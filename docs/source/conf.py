# Configuration file for the Sphinx documentation builder.
#
# For the full list of built-in configuration values, see the documentation:
# https://www.sphinx-doc.org/en/master/usage/configuration.html

# -- Project information -----------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#project-information
import os
import sys
import django

# Add the project root to the Python path
sys.path.insert(0, os.path.abspath('../..'))

# Set up the Django environment
os.environ['DJANGO_SETTINGS_MODULE'] = 'oc_lettings_site.settings'
django.setup()

project = 'Orange County Lettings'
copyright = '2025, Saleh Trissi'
author = 'Saleh Trissi'
release = '1.0.0'

# -- General configuration ---------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#general-configuration

extensions = [
    'sphinx.ext.autodoc',
]

templates_path = ['_templates']
exclude_patterns = []


# -- Options for HTML output -------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#options-for-html-output

html_theme = 'sphinx_rtd_theme'
html_static_path = ['_static']
