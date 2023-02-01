from setuptools import setup, find_packages


setup(
    name='collibra-luigi-client',
    version='0.1.2',
    description="Collibra Luigi with simple 3 tasks for importing assets",
    license='MIT',
    author="collibra",
    author_email='antonio.castelo@collibra.com',
    packages=find_packages(exclude=["logs", "output", "stage"]),
    include_package_data=True,
    url='',
    keywords=["collibra", "luigi"],
    install_requires=['collibra_core', 'collibra_importer', 'cryptography', 'luigi', 'python-dotenv', 'toml', 'requests']
)
