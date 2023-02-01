

import setuptools

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setuptools.setup(
    packages=setuptools.find_packages(),
    author="Noga Mudrik",

    name="basic_functions",
    version="0.0.01",
    
    author_email="<nmudrik1@jhmi.edu>",
    description="very basic functions for data pre-processing and visualization",
    long_description=long_description,
    long_description_content_type="text/markdown",

    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],

    python_requires=">=3.8",
    install_requires = ['numpy', 'matplotlib','scipy','scipy','pandas','webcolors','qpsolvers',
                        'seaborn','colormap','sklearn', 'dill','mat73', 'easydev']
)

