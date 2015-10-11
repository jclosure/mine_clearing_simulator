try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup

config = {
    'description': '',
    'author': 'Joel Holder',
    'url': 'http://github.com/jclosure',
    'download_url': 'Where to download it.',
    'author_email': 'jclosure@gmail.com',
    'version': '0.1',
    'install_requires': ['nose','mockito','sure','pytest','pytest-cov'],
    'packages': ['starfleet'],
    'scripts': [],
    'name': 'starfleet',
    'include_package_data': True,
    'platforms': 'any',
    'test_suite': 'startfleet.tests.test_simulator',
    'extras_require': {
        'tests': ['pytest'],
    }
}

setup(**config)
