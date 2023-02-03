from setuptools import setup

setup(
    name='pysweep',
    version='0.1.0',
    description='Simple minesweeper game for the terminal',
    long_description='Simple minesweeper game for the terminal',
    url='https://github.com/AnttiRae/PySweep',
    author='Antti rae',
    author_email='anttiraework@gmail.com',
    license='MIT',
    entry_points={'console_scripts': ['pysweep = pysweep.__main__:main', ]},

    classifiers=[
        'Programming Language :: Python :: 3',
    ],
)
