from setuptools import setup, find_packages

setup(
    name='sakharnyi_package',
    version='0.1',
    author='Siarhei Sakharnyi',
    description='Combined package for feature extraction, hyperparameter tuning, and validation schema',
    packages=find_packages(),
    install_requires=['numpy', 'scikit-learn', 'hyperopt','pandas', 'copy',\
        'itertools', 're','fuzzywuzzy']
)
