"""GitHub source resolution and bounded read-only HTTP access."""
import json
import os
import re
import subprocess
import tempfile
import http.client
import time
import urllib.error
import urllib.request
from pathlib import Path
from urllib.parse import quote


def choose_release(releases, tag_pattern=None):
    for release in releases:
        tag = release["tag_name"]
        if release.get("draft") or release.get("prerelease"):
            continue
        if re.search(r"(?i)(?:\d|[.\-_])(?:alpha|beta|rc|canary|nightly|preview|dev)(?:[.\-_\d]|$)", tag):
            continue
        if tag_pattern and not re.search(tag_pattern, tag):
            continue
        return release
    return None


def credential_token():
    token = os.environ.get("GH_TOKEN") or os.environ.get("GITHUB_TOKEN")
    if token:
        return token
    if os.name == "nt":
        env = dict(os.environ, GIT_TERMINAL_PROMPT="0", GCM_INTERACTIVE="Never")
        try:
            result = subprocess.run(["git", "credential", "fill"], input="protocol=https\nhost=github.com\n\n",
                                    text=True, capture_output=True, timeout=25, env=env)
            return dict(line.split("=", 1) for line in result.stdout.splitlines() if "=" in line).get("password")
        except (OSError, subprocess.TimeoutExpired):
            return None
    return None


class GitHub:
    def __init__(self, cache_root, token=None):
        self.cache_root = Path(cache_root)
        self.token = token if token is not None else credential_token()

    def _request(self, url):
        headers = {"User-Agent": "agent-prompts/1.0 (+https://github.com/Zhen-Bu-Chuo/agent-prompts)"}
        if url.startswith("https://api.github.com/"):
            headers.update(Accept="application/vnd.github+json", **{"X-GitHub-Api-Version": "2022-11-28"})
            if self.token:
                headers["Authorization"] = "Bearer " + self.token
        for attempt in range(3):
            try:
                with urllib.request.urlopen(urllib.request.Request(url, headers=headers), timeout=30) as response:
                    return response.read()
            except urllib.error.HTTPError as exc:
                if exc.code not in (403, 429, 500, 502, 503, 504) or attempt == 2:
                    raise
                retry = exc.headers.get("Retry-After", "")
                delay = min(30, int(retry)) if retry.isdigit() else (2 ** (attempt + 1))
                time.sleep(delay)
            except (TimeoutError, urllib.error.URLError, http.client.IncompleteRead, ConnectionResetError):
                if attempt == 2:
                    raise
                time.sleep(2 ** (attempt + 1))

    def api(self, path):
        return json.loads(self._request("https://api.github.com/" + path))

    def _immutable_json(self, repo, commit, name, endpoint):
        path = self.cache_root / repo / commit / (name + ".json")
        if path.exists():
            return json.loads(path.read_text(encoding="utf-8"))
        result = self.api(endpoint)
        path.parent.mkdir(parents=True, exist_ok=True)
        path.write_text(json.dumps(result), encoding="utf-8")
        return result

    def repository(self, repo):
        return self.api("repos/" + repo)

    def releases(self, repo):
        # Paginate past nightly/package releases when resolving a stable package tag.
        return self.api(f"repos/{repo}/releases?per_page=100")

    def latest_release(self, repo, tag_pattern=None):
        """Find the newest stable published release without downloading every release body."""
        page = 1
        while page <= 100:
            tags = self.api(f"repos/{repo}/tags?per_page=100&page={page}")
            if not tags:
                return None
            for item in tags:
                tag = item["name"]
                if tag_pattern and not re.search(tag_pattern, tag):
                    continue
                if re.search(r"(?i)(?:\d|[.\-_])(?:alpha|beta|rc|canary|nightly|preview|dev)(?:[.\-_\d]|$)", tag):
                    continue
                try:
                    release = self.api(f"repos/{repo}/releases/tags/{quote(tag, safe='')}")
                except urllib.error.HTTPError as exc:
                    if exc.code == 404:
                        continue
                    raise
                if not release.get("draft") and not release.get("prerelease"):
                    return release
            if len(tags) < 100:
                return None
            page += 1
        return None

    def commit(self, repo, ref):
        return self.api(f"repos/{repo}/commits/{quote(ref, safe='')}")

    def tree(self, repo, commit):
        try:
            tree = self._immutable_json(repo, commit, "tree", f"repos/{repo}/git/trees/{commit}?recursive=1")
        except (urllib.error.HTTPError, urllib.error.URLError, TimeoutError, http.client.IncompleteRead,
                ConnectionResetError) as exc:
            if isinstance(exc, urllib.error.HTTPError) and exc.code < 500:
                raise
            return self._git_tree(repo, commit)
        if not tree.get("truncated"):
            return [x["path"] for x in tree["tree"] if x["type"] == "blob"]

        # GitHub caps a recursive tree response at 100,000 entries. Continue with
        # smaller immutable subtrees so large monorepos still yield a complete tree.
        try:
            root_tree = self.api(f"repos/{repo}/git/trees/{commit}")
        except (urllib.error.HTTPError, urllib.error.URLError, TimeoutError, http.client.IncompleteRead,
                ConnectionResetError):
            return self._git_tree(repo, commit)
        paths = [item["path"] for item in root_tree["tree"] if item["type"] == "blob"]

        def walk(tree_sha, prefix):
            nested = self._immutable_json(repo, tree_sha, "subtree", f"repos/{repo}/git/trees/{tree_sha}?recursive=1")
            if not nested.get("truncated"):
                paths.extend(prefix + "/" + item["path"] for item in nested["tree"] if item["type"] == "blob")
                return
            children = self.api(f"repos/{repo}/git/trees/{tree_sha}")
            for item in children["tree"]:
                path = prefix + "/" + item["path"]
                if item["type"] == "blob":
                    paths.append(path)
                elif item["type"] == "tree":
                    walk(item["sha"], path)

        for item in root_tree["tree"]:
            if item["type"] == "tree":
                try:
                    walk(item["sha"], item["path"])
                except (urllib.error.HTTPError, urllib.error.URLError, TimeoutError):
                    return self._git_tree(repo, commit)
        return paths

    def git_tree(self, repo, commit):
        return self._git_tree(repo, commit)

    def _git_tree(self, repo, commit):
        """Fallback for very large public repositories whose API tree times out.

        Git is asked for commit/tree objects only. No source blob or upstream code is
        checked out or executed; matching source files are still fetched individually.
        """
        with tempfile.TemporaryDirectory(prefix="agent-prompts-tree-") as directory:
            initialized = subprocess.run(["git", "init", "--quiet", directory], capture_output=True,
                                         text=True, timeout=30)
            if initialized.returncode:
                raise RuntimeError(f"git tree init failed: {initialized.stderr.strip()}")
            fetched = subprocess.run(["git", "-C", directory, "fetch", "--quiet", "--filter=blob:none",
                                     "--depth=1", f"https://github.com/{repo}.git", commit],
                                    capture_output=True, text=True, timeout=300)
            if fetched.returncode:
                raise RuntimeError(f"git tree fetch failed for {repo}@{commit}: {fetched.stderr.strip()}")
            verified = subprocess.run(["git", "-C", directory, "rev-parse", "FETCH_HEAD"],
                                      capture_output=True, text=True, timeout=30)
            if verified.returncode or verified.stdout.strip().lower() != commit.lower():
                raise RuntimeError(f"Git returned a different commit for {repo}: {verified.stdout.strip()}")
            listed = subprocess.run(["git", "-C", directory, "ls-tree", "-r", "--name-only", "FETCH_HEAD"],
                                    capture_output=True, text=True, encoding="utf-8", timeout=180)
            if listed.returncode:
                raise RuntimeError(f"git tree listing failed for {repo}@{commit}: {listed.stderr.strip()}")
            paths = listed.stdout.splitlines()
            cache = self.cache_root / repo / commit / "tree.json"
            payload = dict(sha=commit, truncated=False, tree=[dict(path=path, type="blob") for path in paths])
            cache.parent.mkdir(parents=True, exist_ok=True)
            cache.write_text(json.dumps(payload), encoding="utf-8")
            return paths

    def file(self, repo, commit, path):
        from .archive import safe_relative
        relative = safe_relative(path)
        cache = self.cache_root / repo / commit / "files"
        target = cache.joinpath(*relative.parts)
        if target.exists():
            return target.read_bytes().decode("utf-8-sig")
        result = self._request(f"https://raw.githubusercontent.com/{repo}/{commit}/{quote(path, safe='/')}")
        text = result.decode("utf-8-sig")
        target.parent.mkdir(parents=True, exist_ok=True)
        target.write_bytes(result)
        return text
