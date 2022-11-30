# Configuration file for the Sphinx documentation builder.
#
# This file only contains a selection of the most common options. For a full
# list see the documentation:
# https://www.sphinx-doc.org/en/master/usage/configuration.html


def specs(kind: str) -> list:
    """
    Override the specifications for the given types instead of using the Exhale defaults which lack private members.

    :param kind: The type of item being documented. Options are in exhale.utils.AVAILABLE_KINDS.
    :type kind: str
    :return: The list of specifications to use for this item in the reStructuredText file.
    :rtype: list
    """
    if kind == "class" or kind == "struct":
        return list(breathe_default_members)
    return []


# -- Path setup --------------------------------------------------------------

# If extensions (or modules to document with autodoc) are in another directory,
# add these directories to sys.path here. If the directory is relative to the
# documentation root, use os.path.abspath to make it absolute, like shown here.
#
import sys
from pathlib import Path
from exhale.utils import makeCustomSpecificationsMapping

sys.path.insert(0, str(Path("../src/").resolve()))


# -- Project information -----------------------------------------------------

project = "MathLib"
copyright = "2022, Brian Wing"
author = "Brian Wing"


# -- General configuration ---------------------------------------------------

# Add any Sphinx extension module names here, as strings. They can be
# extensions coming with Sphinx (named "sphinx.ext.*") or your custom
# ones.
extensions = [
    "sphinx.ext.intersphinx",
    "sphinx.ext.coverage",
    "sphinx.ext.graphviz",
    "sphinx_multiversion",
    "breathe",
    "exhale"
]

todo_include_todos = True
coverage_show_missing_items = True

smv_branch_whitelist = None
smv_tag_whitelist = r"^v\d+\.\d+\.\d+"

# Breathe configuration.
breathe_projects = {
    "MathLib": "./_build/doxygen/xml"
}
breathe_default_project = "MathLib"

# Remove :private-members: from the below tuple when making docs for external use.
breathe_default_members = (":members:", ":undoc-members:", ":protected-members:", ":private-members:")

# Exhale configuration.
exhale_args = {
    "containmentFolder":      "./_build/api",
    "rootFileName":           "root.rst",
    "doxygenStripFromPath":   "..",
    "fullApiSubSectionTitle": "API",
    "createTreeView":         False,
    "unabridgedOrphanKinds":  {"dir", "file"},
    "exhaleExecutesDoxygen":  True,
    "exhaleDoxygenStdin":     "INPUT = ../include",
    "customSpecificationsMapping": makeCustomSpecificationsMapping(specs)
}

# Tell sphinx what the primary language being documented is.
primary_domain = "cpp"

# Tell sphinx what the pygments highlight language should be.
highlight_language = "cpp"

# Add any paths that contain templates here, relative to this directory.
templates_path = ["_templates"]

# List of patterns, relative to source directory, that match files and
# directories to ignore when looking for source files.
# This pattern also affects html_static_path and html_extra_path.
exclude_patterns = ["_build", "Thumbs.db", ".DS_Store"]


# -- Options for HTML output -------------------------------------------------

# The theme to use for HTML and HTML Help pages.  See the documentation for
# a list of builtin themes.
#
html_theme = "sphinx_rtd_theme"

# Add any paths that contain custom static files (such as style sheets) here,
# relative to this directory. They are copied after the builtin static files,
# so a file named "default.css" will overwrite the builtin "default.css".
html_static_path = ["_static"]
