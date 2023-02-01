import setuptools

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setuptools.setup(
    name="allan_tool",
    version="4.0.0",
    author="Allan Wang",
    author_email="lawther@mails.cust.edu.cn",
    description="p function and t function",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/iwanglei1",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
)