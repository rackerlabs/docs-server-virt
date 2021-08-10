# -*- coding: utf-8 -*-
"""
RACKSPACE TECHNOLOGY SERVER VIRTUALIZATION SOLUTION GUIDE build configuration file.

This file is execfile()d with the current directory set to its
containing dir.

Note that not all possible configuration values are present in this
autogenerated file.

All configuration values have a default; values that are commented out
serve to show the default.
"""

import sys
import os
# import re

try:
    import sphinx_rtd_theme
except ImportError:
    sphinx_rtd_theme = None

try:
    from sphinxcontrib import spelling
except ImportError:
    spelling = None

try:
    import chios
except ImportError:
    chios = None

# If extensions (or modules to document with autodoc) are in another directory,
# add these directories to sys.path here. If the directory is relative to the
# documentation root, use os.path.abspath to make it absolute, like shown here.
# sys.path.insert(0, os.path.abspath('.'))

# -- General configuration ------------------------------------------------

# If your documentation needs a minimal Sphinx version, state it here.
# needs_sphinx = '1.0'

# Add any Sphinx extension module names here, as strings. They can be
# extensions coming with Sphinx (named 'sphinx.ext.*') or your custom
# ones.
extensions = [
    'sphinx.ext.ifconfig',
    'sphinx.ext.todo',
    'sphinx.ext.extlinks'
]

if spelling is not None:
    extensions.append('sphinxcontrib.spelling')

if chios is not None:
    extensions.append('chios.bolditalic')
    extensions.append('chios.remotecode')
    extensions.append('chios.remoteinclude')

# Add any paths that contain templates here, relative to this directory.
templates_path = ['_templates']

# The suffix of source filenames.
source_suffix = ['.rst']

# Add Markdown support
# try:
#    from recommonmark.parser import CommonMarkParser
#    source_suffix.append('.md')
#    source_parsers = {
#        '.md': CommonMarkParser,
#    }
#except ImportError:
#    sys.stdout.write('''
#                     *************************************
#                     Unable to import CommonMarkParser.
#                     Markdown support will not be enabled.
#                     *************************************
#
#                     ''')

# The encoding of source files.
# source_encoding = 'utf-8-sig'

# set ifconfig tags
if not 'CONTENT_ID_BASE' in os.environ or 'build-' in os.environ['CONTENT_ID_BASE']:
    # for Nexus previews, gh-pages, and local builds
    internal = True
else:
    # for Nexus publishing
    internal = False

# The master toctree document.
master_doc = 'index'


# linkcheck options
linkcheck_ignore = ['https://pages.github.rackspace.com*',
                    'https://pitchfork.eco.rackspace.com*']
linkcheck_anchors = False

# General information about the project.
project = 'Rackspace Technology Server Virtualization Solution Guide'
copyright = '2021, Rackspace Technology'

# The version info for the project you're documenting, acts as replacement for
# |version| and |release|, also used in various other places throughout the
# built documents.
#

# The short X.Y version.
version = "1.0"

# The full version, including alpha/beta/rc tags.
release = "1.0"

# Global variables that are replaced by the specified value during the build
# process.
rst_epilog = """
.. |service| replace:: RACKSPACE TECHNOLOGY SERVER VIRTUALIZATION SOLUTION GUIDE
"""

# sphinxcontrib-versioning options
# See https://robpol86.github.io/sphinxcontrib-versioning/settings.html
scv_root_ref = 'master'
scv_overflow = ('-q', )
scv_show_banner = True
scv_banner_main_ref = 'master'
# scv_whitelist_branches = (re.compile(r"\bmaster\b|\bv1[234]\b"),)
# scv_whitelist_tags = ('NIL', )
scv_push_remote = 'internal'
scv_grm_exclude = ('.nojekyll', '.gitignore')

# The language for content autogenerated by Sphinx. Refer to documentation
# for a list of supported languages.
# language = None

# There are two options for replacing |today|: either, you set today to some
# non-false value, then it is used:
# today = ''
# Else, today_fmt is used as the format for a strftime call.
# today_fmt = '%B %d, %Y'

# List of patterns, relative to source directory, that match files and
# directories to ignore when looking for source files.
exclude_patterns = ['_build', 'samples', 'README.rst', 'README.md']

# The reST default role (used for this markup: `text`) to use for all
# documents.
# default_role = None

# If true, '()' will be appended to :func: etc. cross-reference text.
# add_function_parentheses = True

# If true, the current module name will be prepended to all description
# unit titles (such as .. function::).
# add_module_names = True

# If true, sectionauthor and moduleauthor directives will be shown in the
# output. They are ignored by default.
# show_authors = False

# The name of the Pygments (syntax highlighting) style to use.
pygments_style = 'sphinx'

# External link library
extlinks = {
    'rax': ('https://www.rackspace.com/%s', ''),
    'rax-cart': ('https://cart.rackspace.com/%s', ''),
    'rax-special': ('https://%s.rackspace.com/', ''),
    'rax-cloud': ('https://www.rackspace.com/cloud/%s', ''),
    'rax-dev': ('https://developer.rackspace.com/%s', ''),
    'rax-devdocs': ('https://developer.rackspace.com/docs/%s', ''),
    'rax-devguide': ('https:/developer.rackspace.com/docs/%s', ''),
    'rax-api':
    ('https:/developer.rackspace.com/docs/%s/api-reference', ''),
    'rax-git': ('https://github.com/rackspace/%s', ''),
    'mycloud': ('https://mycloud.rackspace.com/%s', ''),
    'rax-glossary': ('https://developer.rackspace.com/docs/glossary/%s', ''),
    'mycloud': ('https://mycloud.rackspace.com/%s', ''),
    'how-to': ('https://support.rackspace.com/how-to/%s', ''),
    'os': ('https://www.openstack.org/%s', ''),
    'os-docs': ('https://docs.openstack.org/%s', ''),
    'os-wiki': ('https://wiki.openstack.org/%s', ''),
    'git-repo': ('https://github.com/rackerlabs/'
                 'docs-core-infra-user-guide/%s', ''),
    'rackerlabs': ('https://github.com/rackerlabs/%s', ''),
    'rocket': ('https://objectrocket.com/%s', '')
}

# A list of ignored prefixes for module index sorting.
# modindex_common_prefix = []

# If true, keep warnings as "system message" paragraphs in the built documents.
# keep_warnings = False


# -- Options for HTML output ----------------------------------------------

# The theme to use for HTML and HTML Help pages.  See the documentation for
# a list of builtin themes.

if sphinx_rtd_theme:
    html_theme = 'sphinx_rtd_theme'
else:
    html_theme = 'default'

# Theme options are theme-specific and customize the look and feel of a theme
# further.  For a list of options available for each theme, see the
# documentation.
html_theme_options = {
    "collapse_navigation" : False,
    "sticky_navigation": True, 
}

# Add any paths that contain custom themes here, relative to this directory.
import sphinx_rtd_theme
html_theme_path = [sphinx_rtd_theme.get_html_theme_path()]

# The name for this set of Sphinx documents.  If None, it defaults to
# "<project> v<release> documentation".
# html_title = 'Rackspace Technology Server Virtualization Solution Guide'

# A shorter title for the navigation bar.  Default is the same as html_title.
# html_short_title = None
html_short_title = 'Rackspace Technology Server Virtualization Solution Guide'

# The name of an image file (relative to this directory) to place at the top
# of the sidebar.
# html_logo = None

# The name of an image file (within the static path) to use as favicon of the
# docs.  This file should be a Windows icon file (.ico) being 16x16 or 32x32
# pixels large.
html_favicon = '_static/favicons/favicon.ico'

# Add any paths that contain custom static files (such as style sheets) here,
# relative to this directory. They are copied after the builtin static files,
# so a file named "default.css" will overwrite the builtin "default.css".
html_static_path = ['_static']
html_style = 'css/styles.css'

# Add any extra paths that contain custom files (such as robots.txt or
# .htaccess) here, relative to this directory. These files are copied
# directly to the root of the documentation.
# html_extra_path = []

# If not '', a 'Last updated on:' timestamp is inserted at every page bottom,
# using the given strftime format.
# html_last_updated_fmt = 'January 25, 2016'
# html_last_updated_fmt = |today|

# Custom sidebar templates, maps document names to template names.
# html_sidebars = {}

# Additional templates that should be rendered to pages, maps page names to
# template names.
# html_additional_pages = {}

# If false, no module index is generated.
# html_domain_indices = True

# If false, no index is generated.
# html_use_index = True

# If true, the index is split into individual pages for each letter.
# html_split_index = False

# If true, links to the reST sources are added to the pages.
# html_show_sourcelink = True

# If true, "Created using Sphinx" is shown in the HTML footer. Default is True.
# html_show_sphinx = True

# If true, "(C) Copyright ..." is shown in the HTML footer. Default is True.
# html_show_copyright = True

# If true, an OpenSearch description file will be output, and all pages will
# contain a <link> tag referring to it.  The value of this option must be the
# base URL from which the finished HTML is served.
# html_use_opensearch = ''

# This is the file name suffix for HTML files (e.g. ".xhtml").
# html_file_suffix = None

# Language to be used for generating the HTML full-text search index.
# Sphinx supports the following languages:
#   'da', 'de', 'en', 'es', 'fi', 'fr', 'hu', 'it', 'ja'
#   'nl', 'no', 'pt', 'ro', 'ru', 'sv', 'tr'
# html_search_language = 'en'

# A dictionary with options for the search language support, empty by default.
# Now only 'ja' uses this config value
# html_search_options = {'type': 'default'}

# The name of a javascript file (relative to the configuration directory) that
# implements a search results scorer. If empty, the default will be used.
# html_search_scorer = 'scorer.js'

# Output file base name for HTML help builder.
htmlhelp_basename = 'Rackspace Technology Server Virtualization Solution Guide'
# this will change the 'paragraph' character to '#'
html_add_permalinks = '#'
