#!/usr/bin/python3
import setuptools

with open("../README.md", "r") as fh:
    long_description = fh.read()

# print(setuptools.find_packages())


setuptools.setup(
    name="TinyMCE-on-pyqt",
    version="0.1.9",
    author="TimTu",
    author_email="ovo-tim@qq.com",
    description="在pyqt中方便的使用TinyMCE",
    include_package_data=True,
    long_description=long_description,
    license='GPL License',
    long_description_content_type="text/markdown",
    url="https://github.com/ovo-Tim/TinyMCE-on-pyqt",
    packages=["TinyMCE_on_Pyqt"],
    install_requires=['PySide6'],
    classifiers=[
        "Programming Language :: Python :: 3",
        "Operating System :: OS Independent",
    ],
)
