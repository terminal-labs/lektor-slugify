# -*- coding: utf-8 -*-
from lektor.pluginsystem import Plugin

from slugify import slugify


class SlugifyPlugin(Plugin):
    name = "Slugify"
    description = u"Lektor plugin that adds a slugify Jinja filter."

    def on_setup_env(self, **extra):
        def slug_filter(txt, **kwargs):
            return slugify(txt, **kwargs)

        self.env.jinja_env.filters["slug"] = slug_filter
