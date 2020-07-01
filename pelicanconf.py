#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

AUTHOR = "PyLadies"
SITENAME = "PyLadies Global Council"
SITEDESCRIPTION = "Learn more about the PyLadies Global Council."
# Removing url in dev config prevents redirection to live site
SITEURL = ""

# plugins
PLUGIN_PATHS = ["pelican-plugins"]
PLUGINS = ["i18n_subsites", "tipue_search"]
JINJA_ENVIRONMENT = {"extensions": ["jinja2.ext.i18n"]}

# theme and theme localization
THEME = "pelican-fh5co-marble"
I18N_GETTEXT_LOCALEDIR = "pelican-fh5co-marble/locale/"
I18N_GETTEXT_DOMAIN = "messages"
I18N_GETTEXT_NEWSTYLE = True
TIMEZONE = "America/Chicago"
DEFAULT_DATE_FORMAT = "%a, %d %b %Y"
I18N_TEMPLATES_LANG = "en_US"
DEFAULT_LANG = "en"
LOCALE = "en_US"

# content paths
PATH = "content"
PAGE_PATHS = ["pages/en"]
ARTICLE_PAGES = ["blog/en"]

# i18n
I18N_SUBSITES = {
    "es": {"PAGE_PATHS": ["pages/es"], "ARTICLE_PATHS": ["blog/es"], "LOCALE": "es_ES"}
}

# logo path, needs to be stored in PATH Setting
LOGO = "/images/pyladies_refresh.png"

# special content
HERO = [
    {
        "image": "/images/hero/pyladies_taiwan.jpg",
        # for multilanguage support, create a simple dict
        "title": {"en": "What is the PyLadies Global Council?", "es": "Algo especial",},
        # img: https://www.flickr.com/photos/turicas/32464219836/in/photolist-QhDetn-RwkZPc-QWSSqb-RsKLkA-QePCCC-RsKBwd-QWTcDm-RkzB9M-RkA6tx-RwmbMV-RwkUhv-QePpy1-RwmgWx-RwmaYk-RsKe7d-RkA5Dg-RsKAA5-QhDkzR-RsJVqG-Rwmape-RkzPfv-RkzNAK-QeNRnN-RwkzGp-RwmyJk-QhDmAD-RhUFmL-sHAnXD-QhCJRT-QhCuSR-RsKB4E-RsK73y-QhDvcB-Rkzjf6-RwkojK-RsKAiw-QeNDXJ-RkzgnT-RkzfL2-QeNwMm-QhCFHZ-QhCwkR-Rwknse-RwkmLz-RhUBNJ-an8mUq-e4nzb1-eu6aTY-pJSyrr-pJRigg
        "text": {
            "en": "The global leadership team for PyLadies.",
            "es": "Algo especial compartir con el publico",
        },
        "links": [
            {"icon": "icon-code", "url": "https://elections.pyladies.com/pages/history.html", "text": "History"}
        ],
    },
    {
        "image": "/images/hero/pyladies_kampala.jpeg",
        # keep it a string if you dont need multiple languages
        "title": "",
        # keep it a string if you dont need multiple languages
        "text": "",
        "links": [],
    },
    {
        "image": "/images/hero/pyladies_auction_2019.jpg",
        # keep it a string if you dont need multiple languages
        "title": "Who is the PyLadies Global Council?",
        # keep it a string if you dont need multiple languages
        "text": "",
        "links": [
            {"icon": "icon-code", "url": "https://elections.pyladies.com/pages/council.html", "text": "Meet the Council"}
        ],
    },
    {
        "image": "/images/hero/pyladies_india.jpg",
        # keep it a string if you dont need multiple languages
        "title": "",
        # keep it a string if you dont need multiple languages
        "text": "",
        "links": [],
    },
    {
        "image": "/images/hero/pyladies_brasil.jpg",
        "title": "How is the PyLadies Global Council selected?",
        "text": "Register to vote!",
        "links": [
            {"icon": "icon-code", "url": "https://elections.pyladies.com/pages/vote.html", "text": "Vote"}
        ],
    },
    {
        "image": "/images/hero/pyladies_seattle.jpeg",
        # keep it a string if you dont need multiple languages
        "title": "",
        # keep it a string if you dont need multiple languages
        "text": "",
        "links": [],
    },
    {
        "image": "/images/hero/pyladies_recife_brasil.jpg",
        "title": "Would you like to join the PyLadies Global Council?",
        "text": "We need you!",
        "links": [
            {"icon": "icon-code", "url": "https://elections.pyladies.com/pages/apply.html", "text": "Apply today!"}
        ],
    },
    {
        "image": "/images/hero/pyladies_tokyo.jpg",
        # keep it a string if you dont need multiple languages
        "title": "",
        # keep it a string if you dont need multiple languages
        "text": "",
        "links": [],
    },
]

# Social widget
SOCIAL = (
    ("Github", "https://www.github.com/pyladies", "https://elections.pyladies.com/docs/elections/images/icons/github.svg"),
    ("Instagram", "https://www.instagram.com/pyladies_global", "https://elections.pyladies.com/docs/elections/images/icons/instagram.svg"),
    ("Slack", "https://slackin.pyladies.com", "https://elections.pyladies.com/docs/elections/images/icons/slack.svg"),
    ("Twitter", "https://www.twitter.com/pyladies", "https://elections.pyladies.com/docs/elections/images/icons/twitter.svg"),
)

# About
ABOUT = {
    "image": "/images/pyladies_refresh.png",
    "mail": "info@pyladies.com",
    # keep it a string if you dont need multiple languages
    "text": {"en": "Learn more about PyLadies.", "es": "Aprende mas de PyLadies"},
    "link": "http://pyladies.com",
    # the address is also taken for google maps
    # "address": "Chicago, Illinois",
    # "phone": "+999-999-9999",
}

# Navigation
DISPLAY_PAGES_ON_MENU = True
DISPLAY_PAGES_ON_HOME = True
DISPLAY_CATEGORIES_ON_MENU = False
DISPLAY_TAGS_ON_MENU = False
USE_FOLDER_AS_CATEGORY = True
PAGE_ORDER_BY = "order"

MENUITEMS = [("Contact", "contact.html")]

DIRECT_TEMPLATES = [
    "index",
    "tags",
    "categories",
    "authors",
    "contact",  # needed for the contact form
]

# Disqus
DISQUS_SHORTNAME = "gitcd-dev"
DISQUS_ON_PAGES = False  # if true its just displayed on every static page, like this you can still enable it per page

# setup google maps
# GOOGLE_MAPS_KEY = "AIzaSyCefOgb1ZWqYtj7raVSmN4PL2WkTrc-KyA"

# DEFAULT_PAGINATION = 10

# Uncomment following line if you want document-relative URLs when developing
# RELATIVE_URLS = True
