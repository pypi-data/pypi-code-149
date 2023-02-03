from setuptools import setup, find_packages

setup(name='codelinescounter',
      version='0.0.3',
      url='https://github.com/AndK17/codelinescounter',
      license='GNU GPL v3',
      author='AndK',
      author_email='karpukhin_av@mail.ru',
      description='Python library for counting lines of python code in file or directory',
      install_requires=['prettytable'],
      packages = find_packages(),
      long_description=open('README.md', encoding='UTF-8').read(),
      long_description_content_type="text/markdown",
      keywords=['count code', 'count lines', 'code lines', 'lines'])