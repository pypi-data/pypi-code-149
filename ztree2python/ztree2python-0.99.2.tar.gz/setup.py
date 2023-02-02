from setuptools import setup

# read the contents of your README file
from pathlib import Path
this_directory = Path(__file__).parent
long_description = (this_directory / "README.md").read_text()

setup(
    name='ztree2python',
    version='0.99.2',
    py_modules=['ztree2python'],
    description='Read z-Tree data files.',
    long_description=long_description,
    long_description_content_type='text/markdown',
    author='Kan Takeuchi',
    author_email='takeuchi.kan@gmail.com',
    url='https://github.com/takekan/ztree2python',
    packages=['ztree2python'], 
    install_requires=['pandas'],
    keywords=['z-Tree', 'z-tree', 'zTree', 'ztree', 'ztree2python', 'ztree2stata', 'economic experiment', 'experimental economics'],
    classifiers=['Intended Audience :: Science/Research'],
)