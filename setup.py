from setuptools import setup

setup(
    name='lektor-slugify',
    version='0.2',
    author=u'Terminal Labs, Michael Verhulst, Joseph Nix',
    author_email='solutions@terminallabs.com',
    description='Adds slugify Jinja filter.',
    url='https://github.com/terminal-labs/lektor-slugify',
    license='BSD-3-Clause',
    py_modules=['lektor_slugify'],
    entry_points={
        'lektor.plugins': [
            'slugify = lektor_slugify:SlugifyPlugin',
        ]
    },
    install_requires=[
        'python-slugify',
    ]
)
