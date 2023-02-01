"""
from distutils.core import setup

setup(
	name 			= 'riyazi',
	version 		= '0.01',
	py_modules  	= ['math', 'stats'],
	author 			= 'mdslauddin',
	author_email 	= 'mdslauddin285@gmail.com',
	url 			= 'aloneweb1.blogspot',
	description		= 'math library',
)





from setuptools import setup, find_packages

setup(
    name='riyazi',
    version='0.1',
    packages=find_packages(),
    install_requires=[
        'numpy',
        'scipy',
    ],
    entry_points={
        'console_scripts': [
            'my-script = my_package.scripts.my_script:main',
        ],
    },
)

"""

