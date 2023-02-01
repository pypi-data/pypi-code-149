from setuptools import setup, find_packages


with open('requirements.txt', 'r') as f:
    REQUIRED_DEP = [i.replace('\n', '') for i in f.readlines()]

setup(
    name='docsetviz',
    version='1.0.2',
    description='Docset Visualization Tool',
    author='yanaenen',
    install_requires=REQUIRED_DEP,
    package_dir={'docsetviz': '.'},
    packages=find_packages(),
    entry_points={
        'console_scripts': [
            'docsetviz=docsetviz.main:main'
        ]
    },
)