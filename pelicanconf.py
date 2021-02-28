#!/usr/bin/env python
# -*- coding: utf-8 -*- #

from pelican.plugins import image_process
import datetime

AUTHOR = "sascha"
SITENAME = "saschakiefer"
SITEURL = ""

BIO = """
            Hi, ich bin Sascha. Ein Ehemann, großer Bruder und Onkel. 
            Ein Kletterer, Rennradfahrer und Mountainbiker. Ein 
            Introvertierter. Ein Softwarearchitekt und Programmierer.
            Ein Stifte- und Papierliebhaber. Einer, der gerne die Welt 
            bereist. Im Camper, auf dem Rad und zu Fuß
           """

PROFILE_IMAGE = "AboutMeImage.png"

PATH = "content"
STATIC_PATHS = ["images", "downloads"]

THEME = "/Users/saschakiefer/git/homepage/pelican-hyde"
FAVICON = "images/SKFavIcon.ico"
COLOR_THEME = "00"
FOOTER_TEXT = "(c) " + str(datetime.date.today().year) + " by Sascha Kiefer"

PLUGIN_PATHS = ["/Users/saschakiefer/git/homepage/pelican-plugins"]
PLUGINS = [
    "image_process",
]

IMAGE_PROCESS_FORCE = True
IMAGE_PROCESS = {
    "article-image": ["scale_in 880 880 True"],
    "article-image-small": ["scale_in 250 250 True"],
    "thumb": ["crop 0 0 50% 50%", "scale_out 150 150 True", "crop 0 0 150 150"],
}

TIMEZONE = "Europe/Berlin"

DEFAULT_LANG = "de"

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None

SOCIAL = (
    ("twitter", "https://twitter.com/saschakiefer"),
    ("linkedin", "https://www.linkedin.com/in/sascha-kiefer-a339997"),
    ("github", "https://github.com/saschakiefer"),
    ("gitlab", "https://gitlab.com/saschakiefersaar"),
)

DEFAULT_PAGINATION = 10

TYPOGRIFY = False
