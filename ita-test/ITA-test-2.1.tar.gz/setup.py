from setuptools import setup, find_packages

classifiers = [
    'Programming Language :: Python :: 3'
]

setup(
    name='ITA-test',
    version='2.1',
    description='Italian tweets analyzer is a tool created for the thesis work at the University of Bari "\Aldo Moro\" '
                'of the course "\Methods for the information retrieval\" that can perform analysis on Italian tweets and it provides several features'
                'This project is an upgraded version of the tool: Hate-Tweet-Map.',
    long_description=open('README.txt').read(),
    url='',
    author='sdvolpicella',
    author_email='davidevolpicella@gmail.com',
    license='',
    classifiers=classifiers,
    keywords='',
    packages=find_packages(),
    install_requires=['']
)