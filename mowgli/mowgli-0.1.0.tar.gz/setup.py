#!/usr/bin/env python

from setuptools import setup, find_packages

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setup(
    name="mowgli",
    version="0.1.0",
    description="Mowgli: Multi Omics Wasserstein inteGrative anaLysIs.",
    long_description=long_description,
    long_description_content_type="text/markdown",
    author="Geert-Jan Huizing, Laura Cantini, Gabriel Peyré",
    url="https://github.com/cantinilab/Mowgli",
    author_email="geert-jan.huizing@ens.fr",
    packages=["mowgli"],
    install_requires=[
        "torch",
        "numpy",
        "pandas",
        "scikit-learn",
        "muon",
        "tqdm",
        "scanpy",
        "anndata",
        "matplotlib",
        "scipy",
        "gprofiler-official",
        "leidenalg",
        "nbsphinx",
        "furo",
    ],
)
