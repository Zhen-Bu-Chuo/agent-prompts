"""Static prompt extraction. Upstream code is parsed as data and never executed."""
import ast
import json
import re
from dataclasses import dataclass

import yaml


def _key_matches(pattern, context):
    return not pattern or re.search(pattern, context, re.IGNORECASE)


@dataclass(frozen=True)
class Fragment:
    key: str
    content: str
    start_line: int
    end_line: int
    kind: str = "static_template"
    notes: str = ""


def _line(source, offset):
    return source.count("\n", 0, offset) + 1


def _python(source, min_chars, key_pattern):
    tree = ast.parse(source)
    results = []
    counts = {}

    def visit(node, context="module"):
        if isinstance(node, (ast.FunctionDef, ast.AsyncFunctionDef, ast.ClassDef)):
            context += "." + node.name
        if isinstance(node, ast.Assign):
            context += "." + ast.unparse(node.targets[0])
        elif isinstance(node, ast.AnnAssign):
            context += "." + ast.unparse(node.target)
        if isinstance(node, ast.Expr) and isinstance(node.value, (ast.Constant, ast.JoinedStr)):
            return  # Module/class/function documentation isn't a runtime prompt.
        if isinstance(node, ast.JoinedStr):
            text = ast.get_source_segment(source, node) or ast.unparse(node)
            match = re.match(r"(?is)^[rubf]*(\"\"\"|'''|\"|')", text)
            if match and text.endswith(match.group(1)):
                text = text[match.end():-len(match.group(1))]
            add(node, context, text, "dynamic_template", "Static Python f-string source; expressions are preserved and have not been evaluated.")
            return  # Avoid extracting literal components of the f-string again.
        if isinstance(node, ast.Constant) and isinstance(node.value, str):
            add(node, context, node.value, "static_template", "Python string decoded by the AST parser; upstream code was not executed.")
            return
        for child in ast.iter_child_nodes(node):
            visit(child, context)

    def add(node, context, text, kind, notes):
        if len(text.strip()) < min_chars or not _key_matches(key_pattern, context):
            return
        counts[context] = counts.get(context, 0) + 1
        results.append(Fragment(f"{context}.{counts[context]}", text, node.lineno, node.end_lineno, kind, notes))

    visit(tree)
    return results


def _quoted_end(source, start):
    quote = source[start]
    i = start + 1
    while i < len(source):
        if source[i] == "\\":
            i += 2
        elif source[i] == quote:
            return i + 1
        else:
            i += 1
    raise ValueError("Unterminated JavaScript string")


def _comment_end(source, start):
    if source.startswith("//", start):
        end = source.find("\n", start)
        return len(source) if end < 0 else end
    end = source.find("*/", start + 2)
    if end < 0:
        raise ValueError("Unterminated JavaScript comment")
    return end + 2


def _regex_start(source, position):
    prefix = source[:position].rstrip()
    previous = prefix[-1:] or ""
    if previous in "=(:,[!?&|{};":
        return True
    return bool(re.search(r"\b(?:return|case|typeof|delete|void|new|in|of|yield|await|else|throw|instanceof|extends)\s*$|=>\s*$", prefix))


def _regex_end(source, start):
    i, in_class = start + 1, False
    while i < len(source) and source[i] not in "\r\n":
        if source[i] == "\\":
            i += 2
        elif source[i] == "[" and not in_class:
            in_class = True
            i += 1
        elif source[i] == "]" and in_class:
            in_class = False
            i += 1
        elif source[i] == "/" and not in_class:
            i += 1
            while i < len(source) and source[i].isalpha():
                i += 1
            return i
        else:
            i += 1
    return start + 1


def _expression_end(source, start):
    depth, i = 1, start
    while i < len(source):
        char = source[i]
        if source.startswith(("//", "/*"), i):
            i = _comment_end(source, i)
        elif source[i] == "/" and _regex_start(source, i):
            i = _regex_end(source, i)
        elif char in "\"'":
            i = _quoted_end(source, i)
        elif char == "`":
            i = _template_end(source, i)
        elif char == "{":
            depth += 1
            i += 1
        elif char == "}":
            depth -= 1
            i += 1
            if depth == 0:
                return i
        else:
            i += 1
    raise ValueError("Unterminated JavaScript interpolation")


def _template_end(source, start):
    i = start + 1
    while i < len(source):
        if source[i] == "\\":
            i += 2
        elif source[i] == "`":
            return i + 1
        elif source.startswith("${", i):
            i = _expression_end(source, i + 2)
        else:
            i += 1
    raise ValueError("Unterminated JavaScript template")


def _js_context(prefix):
    names = re.findall(r"(?:const|let|var|function)\s+(\w+)|[,{]\s*(\w+)\s*:", prefix)
    return next((a or b for a, b in reversed(names)), "template")


def _javascript(source, min_chars, key_pattern, quoted=False):
    results, i, ordinal = [], 0, 0
    while i < len(source):
        if source.startswith(("//", "/*"), i):
            i = _comment_end(source, i)
        elif source[i] == "/" and _regex_start(source, i):
            i = _regex_end(source, i)
        elif source[i] in "\"'":
            end = _quoted_end(source, i)
            content = source[i + 1:end - 1]
            context = _js_context(source[max(0, i - 500):i])
            ordinal += 1
            if quoted and len(content.strip()) >= min_chars and _key_matches(key_pattern, context):
                results.append(Fragment(f"{context}.{ordinal}", content, _line(source, i), _line(source, end - 1),
                                        "source_string_fragment", "Raw JavaScript quoted string body; source escapes and separate concatenation/array fragments are preserved without evaluation."))
            i = end
        elif source[i] == "`":
            end = _template_end(source, i)
            content = source[i + 1:end - 1]
            prefix = source[max(0, i - 500):i]
            context = _js_context(prefix)
            ordinal += 1
            if len(content.strip()) >= min_chars and _key_matches(key_pattern, context):
                dynamic = "${" in content
                results.append(Fragment(f"{context}.{ordinal}", content, _line(source, i), _line(source, end - 1),
                                        "dynamic_template" if dynamic else "static_template",
                                        "Raw JavaScript template body; escapes, expressions and nested templates are preserved without evaluation."))
            i = end
        else:
            i += 1
    return results


def _structured(source, fmt, min_chars, key_pattern):
    data = yaml.safe_load(source) if fmt == "yaml" else json.loads(source)
    results = []
    pattern = key_pattern or r"(?i)(prompt|template|instruction|system_message|human_message|user_message)"

    def visit(value, keys):
        if isinstance(value, dict):
            for key, item in value.items():
                visit(item, keys + [str(key)])
        elif isinstance(value, list):
            for index, item in enumerate(value):
                visit(item, keys + [str(index)])
        elif isinstance(value, str) and len(value.strip()) >= min_chars and _key_matches(pattern, ".".join(keys)):
            # YAML scalar line mapping can be nonliteral; cite the complete source file.
            results.append(Fragment(".".join(keys), value, 1, source.count("\n") + 1,
                                    "structured_template", "Value selected from a structured configuration; line range cites the complete file."))

    visit(data, [])
    return results


def _rust_context(prefix):
    names = re.findall(r"\b(?:const|static|let)\s+(?:mut\s+)?([A-Za-z_]\w*)", prefix)
    return names[-1] if names else "literal"


def _rust(source, min_chars, key_pattern):
    results, i, ordinal = [], 0, 0
    while i < len(source):
        if source.startswith("//", i):
            end = source.find("\n", i)
            i = len(source) if end < 0 else end
        elif source.startswith("/*", i):
            depth, i = 1, i + 2
            while depth and i < len(source):
                if source.startswith("/*", i):
                    depth, i = depth + 1, i + 2
                elif source.startswith("*/", i):
                    depth, i = depth - 1, i + 2
                else:
                    i += 1
            if depth:
                raise ValueError("Unterminated Rust block comment")
        elif source[i] == "r" and i + 1 < len(source) and source[i + 1] in '#"':
            j = i + 1
            while j < len(source) and source[j] == "#":
                j += 1
            if j < len(source) and source[j] == '"':
                hashes = source[i + 1:j]
                close = '"' + hashes
                end = source.find(close, j + 1)
                if end < 0:
                    raise ValueError("Unterminated Rust raw string")
                content = source[j + 1:end]
                prefix = source[max(0, i - 500):i]
                context = _rust_context(prefix)
                ordinal += 1
                if len(content.strip()) >= min_chars and _key_matches(key_pattern, context):
                    results.append(Fragment(f"{context}.{ordinal}", content, _line(source, i), _line(source, end),
                                            "static_template", "Raw Rust string body preserved without compiling or running source."))
                i = end + len(close)
            else:
                i += 1
        elif source[i] == '"':
            end = _quoted_end(source, i)
            content = source[i + 1:end - 1]
            prefix = source[max(0, i - 500):i]
            context = _rust_context(prefix)
            ordinal += 1
            if len(content.strip()) >= min_chars and _key_matches(key_pattern, context):
                results.append(Fragment(f"{context}.{ordinal}", content, _line(source, i), _line(source, end - 1),
                                        "source_string_fragment", "Raw Rust quoted string body; escapes and interpolation placeholders are kept as written, source is not executed."))
            i = end
        elif source[i] == "'" and i + 2 < len(source) and (source[i + 2] == "'" or source[i + 1] == "\\"):
            i = _quoted_end(source, i)
        else:
            i += 1
    return results


def extract(source, fmt, min_chars=80, key_pattern=None):
    if fmt == "raw":
        return [Fragment("document", source, 1, max(1, source.count("\n") + (not source.endswith("\n"))),
                         "template_document", "Original standalone template; runtime placeholders are preserved.")] if source.strip() else []
    if fmt == "python":
        return _python(source, min_chars, key_pattern)
    if fmt in ("js-templates", "js-strings"):
        return _javascript(source, min_chars, key_pattern, quoted=fmt == "js-strings")
    if fmt in ("yaml", "json"):
        return _structured(source, fmt, min_chars, key_pattern)
    if fmt == "rust-strings":
        return _rust(source, min_chars, key_pattern)
    raise ValueError(f"Unsupported extraction format: {fmt}")
