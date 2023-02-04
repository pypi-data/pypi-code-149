import setuptools

setuptools.setup(
    name="test-package-10",
    version="1.0",
    author="xiaoFei",
    author_email="1228372188@jj.com",
    description="",
    long_description="long_description",
    long_description_content_type="text/markdown",
    url="https://abc",
    packages=setuptools.find_packages(),
    classifiers=[
        "Intended Audience :: Developers",
        "License :: OSI Approved :: Apache Software License",
        "Programming Language :: Python",
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "Topic :: Software Development",
    ],
    install_requires=[
    ],
    python_requires='>=3.6',
)