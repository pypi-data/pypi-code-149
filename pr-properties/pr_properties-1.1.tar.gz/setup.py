from distutils.core import setup
import setuptools

packages = ['properties_utils']
setup(name='pr_properties',
      version='1.1',
      author='Franciz',
      packages=packages,
      package_dir={'requests': 'requests'},
      description='This is a read-write properties tool')
