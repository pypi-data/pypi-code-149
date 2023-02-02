from setuptools import setup

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setup(
    name="meoawji",
    version="1.0.1",
    description="Free uptime bot in replit with module !",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://discord.gg/nUXkXEyBBM",
    author="GxdjCoding",
    author_email="meoawcute@gmail.com",
    license="MIT",
    packages=["meoaw"],
    classifiers=[
        "Programming Language :: Python :: 3",
        "Development Status :: 4 - Beta",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
)
