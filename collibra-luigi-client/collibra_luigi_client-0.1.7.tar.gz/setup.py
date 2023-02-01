from setuptools import setup, find_packages


setup(
    name='collibra_luigi_client',
    version='0.1.7',
    description="Collibra Luigi client with simple 3 tasks for importing assets",
    license='MIT',
    author="collibra",
    author_email='antonio.castelo@collibra.com',
    #packages=find_packages(exclude=["logs", "output", "stage"]),
    packages=find_packages('.'),
    package_dir={'': '.'},
    url='',
    keywords=["collibra", "luigi"],
    install_requires=['collibra_core', 'collibra_importer', 'cryptography', 'luigi', 'python-dotenv', 'toml', 'requests']
)
