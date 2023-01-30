
# DO NOT EDIT THIS FILE -- AUTOGENERATED BY PANTS
# Target: envoy.distribution.release:package

from setuptools import setup

setup(**{
    'author': 'Ryan Northey',
    'author_email': 'ryan@synca.io',
    'description': '"Release publishing tool used in Envoy proxy\'s CI"',
    'entry_points': {
        'console_scripts': [
            'envoy.distribution.release=envoy.distribution.release:cmd',
        ],
    },
    'install_requires': (
        'abstracts>=0.0.12',
        'aio.core>=0.9.1',
        'aio.run.runner>=0.3.3',
        'envoy.base.utils>=0.3.9',
        'envoy.github.abstract>=0.0.22',
        'envoy.github.release>=0.0.15',
        'gidgethub',
    ),
    'license': 'Apache Software License 2.0',
    'long_description': """
envoy.distribution.release
==========================

Release publishing tool used in Envoy proxy's CI
""",
    'maintainer': 'Ryan Northey',
    'maintainer_email': 'ryan@synca.io',
    'name': 'envoy.distribution.release',
    'namespace_packages': (
    ),
    'package_data': {
        'envoy.distribution.release': (
            'py.typed',
        ),
    },
    'packages': (
        'envoy.distribution.release',
    ),
    'url': 'https://github.com/envoyproxy/pytooling/tree/main/envoy.distribution.release',
    'version': '0.0.9',
})
