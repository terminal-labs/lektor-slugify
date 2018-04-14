# -*- coding: utf-8 -*-
from lektor.pluginsystem import Plugin

from slugify import slugify

class SlugifyPlugin(Plugin):
    def on_setup_env(self, **extra):
        def slug_filter(txt):
            return slugify(txt)
        self.env.jinja_env.filters['slug'] = slug_filter
