from setuptools import setup, find_packages
import os

here = os.path.abspath(os.path.dirname(__file__))

NAME = "CRClx"
VERSION = '0.0.1'
DESCRIPTION = 'Lightweight library for calculating Cyclic Redundancy Check (CRC) checksums'


def read(fname):
    return open(os.path.join(os.path.dirname(__file__), fname)).read()


LONG_DESCRIPTION = read("README.md")


# Setting up
setup(
    name=NAME,
    version=VERSION,
    author="technician",
    author_email="<mail@xxxxxxxx.com>",
    description=DESCRIPTION,
    long_description_content_type="text/markdown",
    long_description=LONG_DESCRIPTION,
    url="https://github.com/technikian/crc",
    project_urls={
        "Source": "https://github.com/technikian/crc",
    },
    license='MPL',
    license_files=["LICENSE", ],
    packages=find_packages(),
    install_requires=[],  # ['opencv-python', 'pyautogui', 'pyaudio'],
    keywords=['python', NAME, "lightweight", 'crc', 'cyclic', 'redundancy', 'check', "checksum"],
    classifiers=[
        "Development Status :: 1 - Planning",
        "Intended Audience :: Developers",
        'License :: OSI Approved :: Mozilla Public License 2.0 (MPL 2.0)',
        "Programming Language :: Python :: 3",
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
        'Programming Language :: Python :: 3.9',
        'Programming Language :: Python :: 3.10',
        'Programming Language :: Python :: 3.11',
        'Operating System :: OS Independent',
        # "Operating System :: Unix",
        # "Operating System :: MacOS :: MacOS X",
        # "Operating System :: Microsoft :: Windows",
        'Topic :: Software Development :: Embedded Systems',
        "Topic :: Scientific/Engineering",
        "Topic :: Utilities",
    ]
)
