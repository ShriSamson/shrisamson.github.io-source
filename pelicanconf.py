#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

AUTHOR = 'Shri Samson'
SITENAME = 'Shri Samson'
SITEURL = ''

PATH = 'content'

TIMEZONE = 'America/Los_Angeles'		

DEFAULT_LANG = 'en'

THEME = 'notmyidea' #simplest: notmyidea; themes folder themes: themes/theme
#THEME_STATIC_DIR = 'theme' 	default: theme
#CSS_FILE = 'main.css'		default: main.css

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None

# Blogroll
LINKS = (('Pelican', 'http://getpelican.com/'),
         ('Python.org', 'http://python.org/'),
         ('Jinja2', 'http://jinja.pocoo.org/'),
         ('Springboard', 'https://www.springboard.com/'),)

# Social widget
SOCIAL = (('linkedin', 'https://www.linkedin.com/in/shri-samson'),
		('github', 'https://github.com/ShriSamson'),
		('email', 'mailto:ssamson89@gmail.com')	
          )

DEFAULT_PAGINATION = False

# Uncomment following line if you want document-relative URLs when developing
#RELATIVE_URLS = True

MARKUP = ('md', 'ipynb')

PLUGIN_PATHS = ['./plugins']
PLUGINS = ['ipynb.markup']
