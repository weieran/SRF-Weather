# Configuration file for the Sphinx documentation builder.
#
# For the full list of built-in configuration values, see the documentation:
# https://www.sphinx-doc.org/en/master/usage/configuration.html

# -- Project information -----------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#project-information
import os
import sys
import sphinx_rtd_theme

# Add the project source directory to the Python path
sys.path.insert(0, os.path.abspath('../srf_weather'))

# ... other configuration settings ...

# Add the RTD theme
html_theme = 'sphinx_rtd_theme'
html_theme_path = [sphinx_rtd_theme.get_html_theme_path()]


project = 'srf-weather'
copyright = '2023, Andreas Weier'
author = 'Andreas Weier'
release = '0.1.0'

# -- General configuration ---------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#general-configuration

extensions = [
    "sphinx.ext.duration",
    "sphinx.ext.doctest",
    "sphinx.ext.autodoc",
    "sphinx.ext.autosummary",
    "sphinx.ext.intersphinx",
]

intersphinx_mapping = {
    "rtd": ("https://docs.readthedocs.io/en/stable/", None),
    "python": ("https://docs.python.org/3/", None),
    "sphinx": ("https://www.sphinx-doc.org/en/master/", None),
}

templates_path = ['_templates']

# Add the RTD theme
html_theme = 'sphinx_rtd_theme'
html_theme_path = [sphinx_rtd_theme.get_html_theme_path()]

# Tell Sphinx to ignore the Poetry virtual environment
exclude_patterns = ['_build', 'dist', '.tox', 'Thumbs.db', '.DS_Store', '.venv']

# Set the master document
master_doc = 'index'

# Set the path to the source files
source_suffix = '.rst'
source_encoding = 'utf-8'
source_parsers = {
    '.md': 'recommonmark.parser.CommonMarkParser',
}

# Set the path to the output files
html_static_path = ['_static']