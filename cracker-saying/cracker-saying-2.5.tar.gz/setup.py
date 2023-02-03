from setuptools import setup

try:
	import pypandoc
	long_description = pypandoc.convert_file('README.md', 'rst')
	long_description = long_description.replace("\r","") 
except(IOError, ImportError):
	long_description = open('README.md').read()

setup(name='cracker-saying',
version='2.5',
description='A simple pip for designing & designing termux banner.',
log_description = long_description,
long_description_content_type='text/markdown',
author='cracker911181',
author_email='admin@cracker911181.cf',
url='https://pypi.org/project/cracker-saying',
download_url='https://pypi.org/project/cracker-saying',
packages=['cracker_say'],

zip_safe=False)
