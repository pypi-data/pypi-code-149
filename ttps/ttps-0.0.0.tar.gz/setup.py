from setuptools import setup, find_packages

with open("README.md", "r") as fh:
    long_description = fh.read()

setup(
    name="ttps",
    version="0.0.0",
    packages=find_packages(),
    url="",
    license="MIT",
    author="xuewei.chao",
    author_email="xuewei.chao@momenta.ai",
    description="A example demo package",
    long_description=long_description,
    long_description_content_type="text/markdown",
    install_requires=["numpy"],
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires=">=3.7",
    entry_points={
        "console_scripts": [
            "ttps-cli = ttps:my_function",
        ]
    },
)
