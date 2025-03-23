import os
import re
import sys

file_dir = os.path.dirname(__file__)
sys.path.insert(0, os.path.abspath(os.path.join(file_dir, "../../")))

# Project information
project = "Image Machine Learning Research"
copyright = "2025, Luis Kraker"
author = "Luis Kraker"
IMLResearch = "IMLResearch"

# Sphinx extensions
extensions = [
    "sphinx.ext.autodoc",
    "sphinx.ext.napoleon",
    "sphinx.ext.viewcode",
    "sphinxcontrib.bibtex",
]

autosummary_generate = True  # Generate summary tables automatically

# HTML Theme
html_theme = "furo"
# html_theme = "sphinx_rtd_theme"
html_static_path = ["_static"]

# Bibtext file
bibtex_bibfiles = ["references.bib"]

# The master toctree document.
root_doc = "index"

# Extract Version
version = "0.0.0" # Default version
_path = os.path.abspath(f"{__file__}/../../../imlresearch/src/version.py")
with open(_path, encoding="utf-8") as f:
    for line in f:
        match = re.search('__version__ = "([0-9][.][0-9]+[.][0-9]+)"', line)
        if match:
            version = match.group(1)
            break
    else:
        raise Exception(f"Failed to find `__version__ = ...` in {_path}")

# The reST default role (used for this markup: `text`) to use for all documents.
# (This is telling Sphinx to automatically determine the most appropriate role
# for text)
default_role = "any"

# If true, '()' will be appended to :func: etc. cross-reference text.
add_function_parentheses = True

# If true, the current module name will be prepended to all description unit
# titles (such as .. function::).
add_module_names = True

# If true, sectionauthor and moduleauthor directives will be shown in the
# output. They are ignored by default.
show_authors = True

# Substitution reference for .rst files
rst_prolog = f"""
.. |IMLResearch| replace:: {IMLResearch}
.. |version| replace:: {version}
"""
