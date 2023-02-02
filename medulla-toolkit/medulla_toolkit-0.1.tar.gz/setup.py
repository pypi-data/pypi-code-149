from setuptools import setup
setup(name='medulla_toolkit',
      version='0.01',
      description='Toolkit for the Shopfloor endpoints.',
      author='Medulla',
      packages=['toolkit'],
      install_requires=['requests~=2.28.1'],
      zip_safe=False)
