import re
from pathlib import Path
from setuptools import setup, find_packages


def stream_requirements(fd):
    """For a given requirements file descriptor, generate lines of
    distribution requirements, ignoring comments and chained requirement
    files.
    """
    for line in fd:
        cleaned = re.sub(r'#.*$', '', line).strip()
        if cleaned and not cleaned.startswith('-r'):
            yield cleaned


def load_requirements(txt_path):
    """Short helper for loading requirements from a .txt file.

    Parameters
    ----------
    txt_path : Path or str
        Path to the requirements file.

    Returns
    -------
    list
        List of requirements, one list element per line in the text file.
    """
    with Path(txt_path).open() as requirements_file:
        return list(stream_requirements(requirements_file))


# ---------------------------------------------------------------------------- #
#                                   Requirements                               #
# ---------------------------------------------------------------------------- #

ROOT_PATH = Path(__file__).parent
README_PATH = ROOT_PATH / 'README.md'

REQUIREMENTS_PATH = ROOT_PATH / 'requirements' / 'main.txt'
requirements = load_requirements(REQUIREMENTS_PATH)


# ---------------------------------------------------------------------------- #
#                                   Version                                    #
# ---------------------------------------------------------------------------- #
SRC_PATH = ROOT_PATH / 'equal_odds'
VERSION_PATH = SRC_PATH / '_version.py'

with VERSION_PATH.open('rb') as version_file:
    exec(version_file.read())


# ---------------------------------------------------------------------------- #
#                                   SETUP                                      #
# ---------------------------------------------------------------------------- #
setup(
    name='equal-odds',
    version=__version__,

    description='_PACKAGE IN CONSTRUCTION_',
    keywords=['ml', 'optimization', 'fairness'],

    long_description=(README_PATH).read_text(),
    long_description_content_type='text/markdown',

    python_requires='>=3.8',

    packages=find_packages(),    
    install_requires=requirements,

    author='AndreFCruz',
    url='https://github.com/AndreFCruz/equal-odds',

    license='MIT',

    classifiers=[
        'Development Status :: 2 - Pre-Alpha',
        # 'Development Status :: 3 - Alpha',
        'License :: OSI Approved :: MIT License',
        'Intended Audience :: Science/Research',
        'Topic :: Scientific/Engineering :: Artificial Intelligence',
        'Natural Language :: English',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.8',
        'Programming Language :: Python :: 3.9',
        'Programming Language :: Python :: 3.10',
        'Programming Language :: Python :: 3.11',
    ],
)
