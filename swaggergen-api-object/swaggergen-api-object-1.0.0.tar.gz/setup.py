from __future__ import absolute_import
import re
import ast
from setuptools import setup

_version_re = re.compile(r'__version__\s+=\s+(.*)')

with open('swaggergen_api/_version.py', 'rb') as f:
    version = str(ast.literal_eval(_version_re.search(
        f.read().decode('utf-8')).group(1)))

with open('requirements.txt') as f:
    requirements = [line for line in f.read().splitlines() if line]

setup(
    name='swaggergen-api-object',
    description='Generate API Object from Swagger docs.',
    version=version,
    author='CHNJX',
    author_email='360088940@qq.com',
    url='',
    packages=['swaggergen_api'],
    package_data={'templates': ['swaggergen_api/templates/*']},
    include_package_data=True,
    entry_points={
        'console_scripts': [
            'swaggergen_api=swaggergen_api:generate'
        ]
    },
    install_requires=requirements,
    tests_require=['pytest']
)
