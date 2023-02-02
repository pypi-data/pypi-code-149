from setuptools import setup, find_packages
VERSION = '0.0.2'
DESCRIPTION = 'Myles is amazing'

# Setting up
setup(
    name="bighudders",
    version=VERSION,
    author="Edward Hardy",
    author_email="<hardyedward18@gmail.com>",
    description=DESCRIPTION,
    packages=find_packages(),
    install_requires=['pillow'],
    keywords=['python'],
    classifiers=[
        "Development Status :: 3 - Alpha",
        "Intended Audience :: Education",
        "Programming Language :: Python :: 3",
        "Operating System :: Microsoft :: Windows",
    ]
)