from setuptools import setup, find_packages

with open('README.md', 'r') as fh:
    long_description = fh.read()

setup(
    name='cncolors',  # required
    version='0.1.0',
    description='cncolors: the library for Chinese colors',
    long_description=long_description,
    long_description_content_type='text/x-rst',
    author='Feng Zhu',
    author_email='fzhu2e@outlook.com',
    url='https://github.com/fzhu2e/cnc',
    packages=find_packages(),
    include_package_data=True,
    license='MIT',
    zip_safe=False,
    keywords='python, colors',
    classifiers=[
        'Natural Language :: English',
        'Programming Language :: Python :: 3.9',
        'Programming Language :: Python :: 3.10',
    ],
    install_requires=[
        'pandas',
    ],
)
