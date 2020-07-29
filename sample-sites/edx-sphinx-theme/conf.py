import os
import sys

sys.path.append(os.path.join(os.path.dirname(__file__), "demo"))


# -- Project information -----------------------------------------------------

project = "Sphinx Themes Sample"
copyright = "2020, Pradyun Gedam"
author = "Pradyun Gedam"

# -- Extensions --------------------------------------------------------------
extensions = [
    "sphinx.ext.intersphinx",
    "sphinx.ext.autodoc",
    "sphinx.ext.mathjax",
    "sphinx.ext.viewcode",
]

# -- Options for HTML output -------------------------------------------------

# NOTE: All the lines after this marker, are modified during generation.
# !! MARKER !!
import edx_theme
extensions.append("edx_theme")
html_theme = "edx_theme"
html_theme_path = [edx_theme.get_html_theme_path()]