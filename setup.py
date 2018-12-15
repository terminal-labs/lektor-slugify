import ast
import io
import re

from setuptools import setup

with io.open("README.md", "rt", encoding="utf8") as f:
    readme = f.read()

_description_re = re.compile(r"description\s+=\s+(?P<description>.*)")

with open("lektor_slugify.py", "rb") as f:
    description = str(
        ast.literal_eval(_description_re.search(f.read().decode("utf-8")).group(1))
    )

setup(
    author=u"Terminal Labs, Michael Verhulst, Joseph Nix",
    author_email="solutions@terminallabs.com",
    description=description,
    keywords="Lektor plugin static-site slug jinja2 jinja filter",
    license="BSD-3-Clause",
    long_description=readme,
    long_description_content_type="text/markdown",
    name="lektor-slugify",
    py_modules=["lektor_slugify"],
    url="https://github.com/terminal-labs/lektor-slugify",
    version="0.4",
    classifiers=[
        "Environment :: Plugins",
        "Environment :: Web Environment",
        "Framework :: Lektor",
        "License :: OSI Approved :: BSD License",
    ],
    entry_points={"lektor.plugins": ["slugify = lektor_slugify:SlugifyPlugin"]},
    install_requires=["python-slugify>=1.2.6"],
)
