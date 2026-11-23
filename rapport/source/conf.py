"""Configuration du rapport Sphinx.

Génération du rapport, depuis le dossier rapport/ :
    Windows : make.bat html
    Linux, macOS : make html
Le résultat s'ouvre dans rapport/build/html/index.html.
"""

project = "Réseaux bayésiens pour la modélisation du risque"
author = "Antoine"
copyright = "2026, Antoine"
release = "0.1"

language = "fr"

# MyST permet d'écrire les pages en Markdown, lisibles aussi directement sur GitHub.
extensions = [
    "myst_parser",
    "sphinx.ext.mathjax",
]

# $...$ et $$...$$ pour les formules, comme sur GitHub.
myst_enable_extensions = [
    "dollarmath",
]

source_suffix = {
    ".rst": "restructuredtext",
    ".md": "markdown",
}

exclude_patterns = ["_build", "build"]

html_theme = "alabaster"
html_title = "Réseaux bayésiens pour la modélisation du risque"
