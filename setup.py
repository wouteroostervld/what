try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup

config = {
    'description': 'My Project',
    'author': 'Wouter Oosterveld',
    'url': 'https://github.com/Woutertje/what',
    'download_url': 'https://github.com/Woutertje/what/archive/v0.1.1.tar.gz',
    'author_email': 'wouter@fizzyflux.nl',
    'version': '0.1.1',
    'install_requires': ['nose'],
    'packages': ['what'],
    'scripts': [],
    'name': 'what'
}

setup(**config)
