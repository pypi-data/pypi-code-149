from setuptools import setup
from Cython.Build import cythonize
# Note that this file, setup.py, is only being used to perform cython-related build operations
ext_module = cythonize("src/imppkg/harmonic_mean.pyx", language_level="3")  # or "2" or "3str"

setup(ext_modules=ext_module)
