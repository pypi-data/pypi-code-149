from distutils.core import setup
from setuptools import setup, find_packages

setup(
  name = 'pytohm',
  
  packages=find_packages(),#exclude=['__init__']
  #packages = ['pytohm.combined'], 
  
  version = '0.4',
  license= 'MIT',
  description = "Pytohm is a package with Ohm's Law functions, making it easier to work with Ohm's Law in Python.",
  author = 'Yvnee',
  author_email = 'yeseirav@gmail.com',
  url = 'https://github.com/user/Yvnee',
  download_url = 'https://github.com/Yvnee/Pytohm/archive/refs/tags/0.4.tar.gz', 
  keywords = ['OhmsLaw', 'Ohm', 'Resistance'],

  install_requires=[],

  classifiers=[
    'Development Status :: 3 - Alpha',
    'Intended Audience :: Developers',
    'Topic :: Software Development :: Build Tools',
    'License :: OSI Approved :: MIT License',
    'Programming Language :: Python :: 3',
    'Programming Language :: Python :: 3.4',
    'Programming Language :: Python :: 3.5',
    'Programming Language :: Python :: 3.6'
  ],
)