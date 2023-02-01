import setuptools
#import wget
from setuptools import setup


#URL = "https://gitlab.com/arep-dev/pyViewFactor/-/raw/main/README.md?inline=false"
#response = wget.download(URL, "README.md")
with open('README.md') as f:
    long_description = f.read()


setuptools.setup(
    name="pyviewfactor",
    version="0.0.13",
    author="Mateusz BOGDAN, Edouard WALTHER, Marc ALECIAN, Mina CHAPON",
    description="A python library to calculate numerically exact radiation view factors between planar faces.",
    packages=["pyviewfactor"],
    readme = "README.md",
    long_description=long_description,
    long_description_content_type='text/markdown',  # This is important!
    url='https://gitlab.com/arep-dev/pyViewFactor/',
    license='MIT',
    project_urls={
        "documentation" : "https://arep-dev.gitlab.io/pyViewFactor/",
        "bug tracker": "https://gitlab.com/arep-dev/pyViewFactor/-/issues",
        "repository ": "https://gitlab.com/arep-dev/pyViewFactor/",
    },
    keywords='radiative-transfer radiation vtk geometry ViewFactor STL visibility',
    install_requires=[
        'pandas',
        'pyvista',
        'numba',
        'scipy'
    ],
)
