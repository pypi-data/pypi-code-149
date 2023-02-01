import setuptools


with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()
NAME = 'JIT'
VERSION = '0.2.7'

PACKAGES = setuptools.find_packages()
setuptools.setup(
    name=NAME,
    version=VERSION,
    description='This is a package for my just in time',
    long_description=long_description,
    author='fastbiubiu',
    author_email='fastbiubiu@163.com',
    url='https://github.com/NocoldBob/JIT',
    # package_dir=PACKAGE_DIR,
    include_package_data=True,
    packages=PACKAGES,
    classifiers=[
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.6",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3',
)
