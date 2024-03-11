# Configuration file for the Sphinx documentation builder.

# -- Project information

project = "Section Box"
copyright = "2024, Ruben Messerschmidt"
author = "Ruben Messerschmidt"

release = "2.0.15"
version = "2.0.15"

# -- General configuration

extensions = [
    "sphinx.ext.duration",
    "sphinx.ext.doctest",
    "sphinx.ext.autodoc",
    "sphinx.ext.autosummary",
    "sphinx.ext.intersphinx",
    "sphinx.ext.autosectionlabel",
    "sphinx_rtd_theme",
]

autosectionlabel_prefix_document = True

intersphinx_mapping = {
    "python": ("https://docs.python.org/3/", None),
    "sphinx": ("https://www.sphinx-doc.org/en/master/", None),
}
intersphinx_disabled_domains = ["std"]

templates_path = ["_templates"]

# -- Options for HTML output

html_theme = "sphinx_rtd_theme"

# -- Options for EPUB output
epub_show_urls = "footnote"
