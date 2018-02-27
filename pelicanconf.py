#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

AUTHOR = 'Marianna Foos'
SITENAME = "I'd rather be eating"
SITEURL = 'https://mfoos.github.io/blog'

PATH = 'content'
STATIC_PATHS = ['pdfs', 'pages']
ARTICLE_PATHS = ['pages']

TIMEZONE = 'America/New_York'

DEFAULT_LANG = 'en'

THEME = 'voidy-bootstrap'
#THEME = 'notmyidea'

OUTPUT_SOURCES = False

# Feed generation is usually not desired when developing
FEED_DOMAIN = SITEURL
FEED_ALL_ATOM = 'feeds/all.atom.xml'
FEED_ALL_RSS = 'feeds/all.rss.xml'

#FEED_ALL_ATOM = None
#CATEGORY_FEED_ATOM = None
#TRANSLATION_FEED_ATOM = None
#AUTHOR_FEED_ATOM = None

# Blogroll
LINKS = (('https://mfoos.github.io', 'https://mfoos.github.io'),
         ('Pelican', 'http://getpelican.com/'),
         ('PyLadies Boston', 'http://boston.pyladies.com/'),
         ('R-Ladies Boston', 'https://rladies.github.io/Boston'),
         ('R-Ladies', 'https://rladies.org/'),
         ('Data Carpentry', 'http://www.datacarpentry.org/'),
         ('Jennifer Konikowski', 'http://www.jenniferkonikowski.com/'),
         ('Getting Comfortable With Being Uncomfortable','http://www.smellyeahcandleco.com/blog-2/'),
         ('Getting Ready To Go', 'http://www.gettingreadytogo.net/'),)

# Social widget
SOCIAL = (('Twitter', 'http://www.twitter.com/mariannafoos','fa fa-twitter-square fa-fw fa-lg'),)

DEFAULT_PAGINATION = 10

# Uncomment following line if you want document-relative URLs when developing
#RELATIVE_URLS = True

# voidy-bootstrap settings
CUSTOM_ARTICLE_FOOTERS = ("taglist.html",)

SIDEBAR = "sidebar.html"
