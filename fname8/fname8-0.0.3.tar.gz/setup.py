from setuptools import setup

setup(
   name='fname8',
   version='0.0.3',
   description='A script to check for PEP 8 file naming conventions',
   author='Spencer Taylor-Brown',
   author_email='spencer@spencertaylorbrown.uk',
   packages=['fname8'],
   entry_points={
      'console_scripts': [
          'fname8=fname8.pep8_filename:main'
      ]
   }
)
