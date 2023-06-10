# Configuration file for the Sphinx documentation builder.

# -- Project information

project = 'Nya-JS'
copyright = '2023, Cat'
author = 'Cat'

release = '0.2'
version = '0.3.0'

# -- General configuration

extensions = [
    'sphinx.ext.duration',
    'sphinx.ext.doctest',
    'sphinx.ext.autodoc',
    'sphinx.ext.autosummary',
    'sphinx.ext.intersphinx',
]

intersphinx_mapping = {
    'python': ('https://docs.python.org/3/', None),
    'sphinx': ('https://www.sphinx-doc.org/en/master/', None),
}
intersphinx_disabled_domains = ['std']

templates_path = ['_templates']

# -- Options for HTML output

html_theme = 'sphinx_material'

# Material theme options (see theme.conf for more information)
html_theme_options = {
    # Set the name of the project to appear in the navigation.
    'nav_title': 'Project Name',
    # Set you GA account ID to enable tracking
    'google_analytics_account': 'UA-XXXXX',
    # Specify a base_url used to generate sitemap.xml. If not
    # specified, then no sitemap will be built.
    'base_url': 'https://project.github.io/project',
    # Set the color and the accent color
    'color_primary': 'blue',
    'color_accent': 'light-blue',
    # Set the repo location to get a badge with stats
    'repo_url': 'https://github.com/project/project/',
    'repo_name': 'Project',
    # Visible levels of the global TOC; -1 means unlimited
    'globaltoc_depth': 3,
    # If False, expand all TOC entries
    'globaltoc_collapse': False,
    # If True, show hidden TOC entries
    'globaltoc_includehidden': False,
}

# -- Options for EPUB output
epub_show_urls = 'footnote'
