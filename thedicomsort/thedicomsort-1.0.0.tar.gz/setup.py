# -*- coding: utf-8 -*-
from setuptools import setup

modules = \
['dicomsort']
install_requires = \
['pydicom>=2.3.1,<3.0.0']

entry_points = \
{'console_scripts': ['dicomsort = dicomsort:main']}

setup_kwargs = {
    'name': 'thedicomsort',
    'version': '1.0.0',
    'description': 'The original best and only project to provide custom sorting and renaming of DICOM files',
    'long_description': 'dicomsort\n=========\n\nA project to provide custom sorting and renaming of dicom files\n\n\nDescription\n-----------\n\nGiven DICOM files in a random folder structure, this program copies all into a user-defined folder hierarchy, creating folders as necessary and changing DICOM file names to be more meaningful.\n\nThe user can define the target folder structure and file naming by using a string consisting of concatenated tag names (like \'PatientName\'), underscores and slashes.\nThe last part of the string (as separated by slashes) denotes the naming convention for the file parts.\n\nAn Example: a target string of\n \'Modality/PatientName_PatientID\'\nmeans that all DICOM images are arranged in a base folder and named by PatientName_PatientID,\nfollowed by an underscore and a unique number for every file that falls into the same category (and is not the same..?)\n\ndicomsort returns with a count for both DICOM files organized and non-DICOM (or invalid DICOM) files skipped.\nIt aborts with an error if it is to overwrite any existing file.\n\n\nUsage\n-----\n\n```\n% dicomsort.py --help\ndicomsort [options...] sourceDir targetDir/<patterns>\n\n where [options...] can be:\n    [-z,--compressTargets] - create a .zip file in the target directory\n    [-d,--deleteSource] - remove source files/directories after sorting\n    [-f,--forceDelete] - remove source without confirmation\n    [-k,--keepGoing] - report but ignore dupicate target files\n    [-v,--verbose] - print diagnostics while processing\n    [-s,--symlink] - create a symlink to dicom files in sourceDir instead of copying them\n    [-t,--test] - run the built in self test (requires internet)\n    [-u,--unsafe] - do not replace unsafe characters with \'_\' in the path\n    [--help] - print this message\n\n where sourceDir is directory to be scanned or "" (null string) to read file list from stdin\n\n where targetDir/<patterns...> is a string defining the output file and directory\n names based on the dicom tags in the file.\n\nIf patterns are not specified, the following default is used:\n \n  %PatientName-%Modality%StudyID-%StudyDescription-%StudyDate/%SeriesNumber_%SeriesDescription-%InstanceNumber.dcm\n\nExample 1:\n\n  dicomsort data sorted/%PatientName/%StudyDate/%SeriesDescription-%InstanceNumber.dcm\n\n  could create a folder structure like:\n\n  sorted/JohnDoe/2013-40-18/FLAIR-2.dcm\n\nExample 2:\n\n  find DicomSourceDir/ | grep "IMA$" | dicomsort -s "" DicomTargetDir\n\n  would scan DicomSourceDir for file pathnames ending in IMA and create an\n  output directory DicomTargetDir. The folder structure will be created using\n  the default pattern with symbolic links to the source dicom data files.\n```\n\nRequires\n========\nPython 2.x or 3.x\n\npydicom\n',
    'author': 'Steve Pieper',
    'author_email': 'pieper@isomics.com',
    'maintainer': 'None',
    'maintainer_email': 'None',
    'url': 'None',
    'py_modules': modules,
    'install_requires': install_requires,
    'entry_points': entry_points,
    'python_requires': '>=3.7,<4.0',
}


setup(**setup_kwargs)
