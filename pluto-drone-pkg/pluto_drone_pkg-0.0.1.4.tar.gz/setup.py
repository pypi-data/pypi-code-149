from setuptools import setup, find_packages
import os

here = os.path.abspath(os.path.dirname(__file__))


VERSION = '0.0.1.4'
DESCRIPTION = 'Pluto drone'
# LONG_DESCRIPTION = 'Long Description'

# Setting up
setup(
    name="pluto_drone_pkg",
    version=VERSION,
    author="Aman Singh, Ayush Singh, Raj Surya",
    author_email="ayush.lively2001@gmail.com",
    description=DESCRIPTION,
    # long_description_content_type="text/markdown",
    # long_description=long_description,
    packages=find_packages(),
    install_requires=['keyboard', 'numpy', 'opencv-python', 'sockets'],
    keywords=['python', 'video', 'stream', 'video stream', 'camera stream', 'sockets'],
    classifiers=[
        "Development Status :: 1 - Planning",
        "Intended Audience :: Developers",
        "Programming Language :: Python :: 3",
        "Operating System :: Unix",
        "Operating System :: MacOS :: MacOS X",
        "Operating System :: Microsoft :: Windows",
    ]
)