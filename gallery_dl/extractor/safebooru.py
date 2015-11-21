# -*- coding: utf-8 -*-

# Copyright 2015 Mike Fährmann
#
# This program is free software; you can redistribute it and/or modify
# it under the terms of the GNU General Public License version 2 as
# published by the Free Software Foundation.

"""Extract image-urls from http://safebooru.org/"""

from . import booru

class SafebooruExtractor(booru.XMLBooruExtractor):
    """Base class for safebooru extractors"""

    category = "safebooru"
    api_url = "http://safebooru.org/index.php"

    def setup(self):
        self.params.update({"page":"dapi", "s":"post", "q":"index"})

    def update_page(self, reset=False):
        if reset is False:
            self.params["pid"] += 1
        else:
            self.params["pid"] = 0

class SafebooruTagExtractor(SafebooruExtractor, booru.BooruTagExtractor):
    """Extract images from safebooru based on search-tags"""
    pattern = [r"(?:https?://)?(?:www\.)?safebooru\.org/(?:index\.php)?\?page=post&s=list&tags=([^&]+)"]

class SafebooruPostExtractor(SafebooruExtractor, booru.BooruPostExtractor):
    """Extract single images from safebooru"""
    pattern = [r"(?:https?://)?(?:www\.)?safebooru\.org/(?:index\.php)?\?page=post&s=view&id=(\d+)"]
