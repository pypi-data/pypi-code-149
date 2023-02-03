from setuptools import setup, find_packages
from os.path import join, dirname

import uniqchars_pac

with open("requirements.txt") as dependency:
    requirements = dependency.read()

setup(
    name='uniqchars_pac',
    version=uniqchars_pac.__version__,
    author="Dihtiar Vadym",
    description="Count of uniq chars in string package",
    long_description=open(join(dirname(__file__), 'README.md')).read(),
    long_description_content_type="text/markdown",
    packages=find_packages(),
    install_requires=requirements,
    python_requires='>=3.8',
    include_package_data=True,
    test_suite='tests',
    entry_points={
        'console_scripts':
            [
                # 'uniqchars_pac = uniqchars_pac.core:print_message',
                'main = uniqchars_pac.app.app:main'
            ]
    },
    classifiers=[
        "Programming Language :: Python :: 3.8",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
)
