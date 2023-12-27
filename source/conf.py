import os
import sys

sys.path.append(os.path.abspath("."))

extensions = [
        "sphinx.ext.mathjax",
]

project = "My Sphinx Theme"
author = "Naoki Hori"
copyright = f"2023, {author}"

html_theme = "mysphinxtheme"
html_theme_path = ["."]
html_theme_options = {
        "description": "An easily-hackable Sphinx theme",
        "github_repo": "https://github.com/NaokiHori/MySphinxTheme",
}

mathjax_path = "https://cdn.jsdelivr.net/npm/mathjax@2/MathJax.js?config=TeX-AMS-MML_HTMLorMML"

