# lektor-slugify

[![PyPI version](https://badge.fury.io/py/lektor-slugify.svg)](https://pypi.org/project/lektor-slugify/)
<a href="https://github.com/ambv/black"><img alt="Code style: black" src="https://img.shields.io/badge/code%20style-black-000000.svg"></a>

This is a Lektor plugin that provides a simple template filter that transforms a (unicode) string into a slug.

Usage: `{{ var|slug }}`

Advanced usage: The `|slug` filter can also accept keyword arguements that are passed to python-slugify. That means you have the option of doing, for example, `{{ var|slug(lowercase=False) }}` to preserve case sensitivity.

This is a simple use of the Python package [python-slugify](https://github.com/un33k/python-slugify).
