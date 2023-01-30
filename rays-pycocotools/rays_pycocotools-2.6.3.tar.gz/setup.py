from setuptools import dist, setup, Extension


install_requires = [
    'setuptools>=18.0',
    'cython>=0.27.3',
    'numpy>=1.16.2'
]

dist.Distribution().fetch_build_eggs(install_requires)


import numpy as np


# To compile and install locally run "python setup.py build_ext --inplace"
# To install library to Python site-packages run "python setup.py build_ext install"

ext_modules = [
    Extension(
        'rays_pycocotools._mask',
        sources=['common/maskApi.c', 'rays_pycocotools/_mask.pyx'],
        include_dirs = [np.get_include(), 'common'],
        extra_compile_args=['-Wno-cpp', '-Wno-unused-function', '-std=c99'],
    )
]

setup(
    name='rays_pycocotools',
    packages=['rays_pycocotools'],
    package_dir={'rays_pycocotools': 'rays_pycocotools'},
    description="Wrapper of pycocotools that correctly installs with pip.",
    long_description=open("README.md").read(),
    extras_require={
        'all': ['matplotlib>=2.1.0']
    },
    version='2.6.3',
    ext_modules=ext_modules,
    python_requires='>=3.6',
)
