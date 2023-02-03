from setuptools import setup


with open("README.md", "r") as readme_file:
    long_description = readme_file.read()


setup(
    name='gmi_okx',
    version='0.1',
    packages=['okx'],
    author="GetMoney Inc.",
    author_email='get.money.inc.official@gmail.com',
    description="Interface to interact with OKX by GetMoney Inc.",
    long_description=long_description,
    long_description_content_type='text/markdown',
    url='https://github.com/get-money-inc/okx-py',
    install_requires=[
        'requests>=2.28.2',
        'gmi-utils>=0.1.8',
    ],
)
