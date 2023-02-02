from setuptools import setup, find_packages
from os.path import join, dirname

import woocatpacnew

install_requires = ['Flask==0.8']

setup(
    name='woocatpacnew',
    version=woocatpacnew.__version__,
    include_package_data=True,
    packages=find_packages(),
    test_suite='tests',
    long_description=open(join(dirname(__file__), 'README.md')).read(),
    entry_points={
        'console_scripts':
            [
                'woocatpacnew = woocatpacnew.core:print_message',
                'serve = woocatpacnew.web:run_server'
            ]
    }
)
