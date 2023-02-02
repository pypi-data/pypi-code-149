from setuptools import setup, find_packages


with open("README.md", "r") as readme_file:
    long_description = readme_file.read()


setup(
    name='gmi_utils',
    version='0.1',
    author="GetMoney Inc.",
    author_email='get.money.inc.official@gmail.com',
    description="Utils used by GetMoney Inc.",
    long_description=long_description,
    long_description_content_type='text/markdown',
    packages=find_packages('pkg'),
    package_dir={'': 'pkg'},
    url='https://github.com/get-money-inc/utils-py',
)
