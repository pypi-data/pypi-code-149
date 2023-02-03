from setuptools import setup, find_packages

setup(
    name='githubdown',
    version='0.0.1',
    description='Download files and folders from Github',
    long_description='Download files and folders from Github with automated parsing of urls',
    packages=find_packages(),
    entry_points={"console_scripts": ['githubdown=githubdown.githubdown:main']},
    python_requires='>=3.6',)
