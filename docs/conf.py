# Configuration file for the Sphinx documentation builder.
#
# For the full list of built-in configuration values, see the documentation:
# https://www.sphinx-doc.org/en/master/usage/configuration.html

# -- Project information -----------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#project-information

project = "qcs-api-client"
copyright = "2026, Rigetti Computing"
author = "Rigetti Computing"

# The full version, including alpha/beta/rc tags
with open("../pyproject.toml") as pyproj:
    for line in pyproj:
        if line.startswith("version"):
            start = line.index('"') + 1
            end = line.rindex('"')
            release = line[start:end]
            break
    else:
        raise ValueError("No version found in pyproject.toml")

# -- General configuration ---------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#general-configuration

extensions = [
    "autoapi.extension",
    "sphinx.ext.napoleon",
    "myst_parser",
]

source_suffix = {
    ".rst": "restructuredtext",
    ".txt": "markdown",
    ".md": "markdown",
}

# Document Python Code
autoapi_type = "python"
autoapi_python_class_content = "both"
autoapi_dirs = ["../qcs_api_client"]
autoapi_options = [
    "members",
    "undoc-members",
    "show-inheritance",
    "show-module-summary",
    "special-members",
    "imported-members",
]
autoapi_generate_api_docs = True

exclude_patterns = ["_build", "Thumbs.db", ".DS_Store"]

# -- Options for HTML output -------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#options-for-html-output

html_theme = "furo"
html_theme_options = {
    "light_css_variables": {
        "color-brand-primary": "#00b5ad",
        "color-problematic": "#66d3ce",
        "color-brand-content": "#3d47d9",
    },
    "dark_css_variables": {
        "color-brand-content": "#8b91e8",
    },
}
