from setuptools import setup

from pathlib import Path

this_directory = Path(__file__).parent
long_description = (this_directory / "README.md").read_text()

setup(
    name="Notesh",
    version="0.2",
    description="About NoteSH fully functional sticky notes App in your Terminal!",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="http://github.com/Cvaniak/Notesh",
    author="Cvaniak",
    author_email="igna.cwaniak@gmail.com",
    packages=["notesh"],
    python_requires='>=3.7, <4',
    install_requires=["textual==0.9.1"],
    entry_points={"console_scripts": ["notesh=notesh.command_line:run"]},
    package_data={"notesh": ["*.css", "notesh/*.css"]},
    include_package_data=True,
    zip_safe=False,
)
