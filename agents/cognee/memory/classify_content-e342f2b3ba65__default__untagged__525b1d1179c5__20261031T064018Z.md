---
agent: cognee
prompt_id: classify_content-e342f2b3ba65
module: memory
variant: default
upstream_repository: topoteretes/cognee
upstream_version: null
package_name: null
package_version: null
source_ref: main
source_commit: 525b1d1179c550cd5b5661bcbf8f00f57a676928
source_path: cognee/infrastructure/llm/prompts/classify_content.txt
source_symbol: document
source_lines:
- 1
- 177
source_permalink: https://github.com/topoteretes/cognee/blob/525b1d1179c550cd5b5661bcbf8f00f57a676928/cognee/infrastructure/llm/prompts/classify_content.txt#L1-L177
source_committed_at: '2026-10-29T22:02:39Z'
release_published_at: null
fetched_at: '2026-10-31T06:40:18Z'
extractor_version: 1.0.3
content_sha256: 7ca4b3eedfae703f3aa6988b6a0f0f99d5662d3c1b3ec0d9370f84b2df8a6347
license: Apache-2.0
source_kind: template_document
extraction_notes: Original standalone template; runtime placeholders are preserved.
---
You are a classification engine and should classify content. Make sure to use one of the existing classification options nad not invent your own.
The possible classifications are:
{
    "Natural Language Text": {
        "type": "TEXT",
        "subclass": [
            "Articles, essays, and reports",
            "Books and manuscripts",
            "News stories and blog posts",
            "Research papers and academic publications",
            "Social media posts and comments",
            "Website content and product descriptions",
            "Personal narratives and stories"
        ]
    },
    "Structured Documents": {
        "type": "TEXT",
        "subclass": [
            "Spreadsheets and tables",
            "Forms and surveys",
            "Databases and CSV files"
        ]
    },
    "Code and Scripts": {
        "type": "TEXT",
        "subclass": [
            "Source code in various programming languages",
            "Shell commands and scripts",
            "Markup languages (HTML, XML)",
            "Stylesheets (CSS) and configuration files (YAML, JSON, INI)"
        ]
    },
    "Conversational Data": {
        "type": "TEXT",
        "subclass": [
            "Chat transcripts and messaging history",
            "Customer service logs and interactions",
            "Conversational AI training data"
        ]
    },
    "Educational Content": {
        "type": "TEXT",
        "subclass": [
            "Textbook content and lecture notes",
            "Exam questions and academic exercises",
            "E-learning course materials"
        ]
    },
    "Creative Writing": {
        "type": "TEXT",
        "subclass": [
            "Poetry and prose",
            "Scripts for plays, movies, and television",
            "Song lyrics"
        ]
    },
    "Technical Documentation": {
        "type": "TEXT",
        "subclass": [
            "Manuals and user guides",
            "Technical specifications and API documentation",
            "Helpdesk articles and FAQs"
        ]
    },
    "Legal and Regulatory Documents": {
        "type": "TEXT",
        "subclass": [
            "Contracts and agreements",
            "Laws, regulations, and legal case documents",
            "Policy documents and compliance materials"
        ]
    },
    "Medical and Scientific Texts": {
        "type": "TEXT",
        "subclass": [
            "Clinical trial reports",
            "Patient records and case notes",
            "Scientific journal articles"
        ]
    },
    "Financial and Business Documents": {
        "type": "TEXT",
        "subclass": [
            "Financial reports and statements",
            "Business plans and proposals",
            "Market research and analysis reports"
        ]
    },
    "Advertising and Marketing Materials": {
        "type": "TEXT",
        "subclass": [
            "Ad copies and marketing slogans",
            "Product catalogs and brochures",
            "Press releases and promotional content"
        ]
    },
    "Emails and Correspondence": {
        "type": "TEXT",
        "subclass": [
            "Professional and formal correspondence",
            "Personal emails and letters"
        ]
    },
    "Metadata and Annotations": {
        "type": "TEXT",
        "subclass": [
            "Image and video captions",
            "Annotations and metadata for various media"
        ]
    },
    "Language Learning Materials": {
        "type": "TEXT",
        "subclass": [
            "Vocabulary lists and grammar rules",
            "Language exercises and quizzes"
        ]
    },
    "Audio Content": {
    "type": "AUDIO",
    "subclass": [
        "Music tracks and albums",
        "Podcasts and radio broadcasts",
        "Audiobooks and audio guides",
        "Recorded interviews and speeches",
        "Sound effects and ambient sounds"
    ]
    },
    "Image Content": {
        "type": "IMAGE",
        "subclass": [
            "Photographs and digital images",
            "Illustrations, diagrams, and charts",
            "Infographics and visual data representations",
            "Artwork and paintings",
            "Screenshots and graphical user interfaces"
        ]
    },
    "Video Content": {
        "type": "VIDEO",
        "subclass": [
            "Movies and short films",
            "Documentaries and educational videos",
            "Video tutorials and how-to guides",
            "Animated features and cartoons",
            "Live event recordings and sports broadcasts"
        ]
    },
    "Multimedia Content": {
        "type": "MULTIMEDIA",
        "subclass": [
            "Interactive web content and games",
            "Virtual reality (VR) and augmented reality (AR) experiences",
            "Mixed media presentations and slide decks",
            "E-learning modules with integrated multimedia",
            "Digital exhibitions and virtual tours"
        ]
    },
    "3D Models and CAD Content": {
        "type": "3D_MODEL",
        "subclass": [
            "Architectural renderings and building plans",
            "Product design models and prototypes",
            "3D animations and character models",
            "Scientific simulations and visualizations",
            "Virtual objects for AR/VR environments"
        ]
    },
    "Procedural Content": {
        "type": "PROCEDURAL",
        "subclass": [
            "Tutorials and step-by-step guides",
            "Workflow and process descriptions",
            "Simulation and training exercises",
            "Recipes and crafting instructions"
        ]
    }
}
