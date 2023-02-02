from setuptools import setup, find_packages


with open("README.md", "r", encoding="utf-8") as wa:
    long_description = wa.read()

setup(
    name='wammodels',
    version='0.0.6',
    author="Felipe Ardila (WorldArd)",
    description="library for customization modeling .WA",
    include_package_data=True,
    long_description = long_description,
    long_description_content_type="text/markdown",
    packages=["wammodels"],
    install_requires=[
        'pandas',
        'numpy',
        'statsmodels',
        'patsy',
        'plotly',
        
    ],
)