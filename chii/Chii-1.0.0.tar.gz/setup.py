from setuptools import setup


with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setup(
    name="Chii",
    version="1.0.0",
    packages=["chii"],
    description="",
    long_description=long_description,
    long_description_content_type="text/markdown",
    install_requires=[
        "requests",
        "python-telegram-bot==13.15",
    ],
)
