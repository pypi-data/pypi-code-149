from setuptools import setup

with open("README", 'r') as f:
    long_description = f.read()

setup(name='pyNebula',
version='0.6.1',
description='A Powerfull Encryptor For Encrypt Python Code. It Has No Decode Function. It Directly Exicute Your Encrypted Code',
license="GNU General Public License v3.0",
long_description=long_description,
author='cracker911181',
url='https://github.com/cracker911181/pyNebula',
packages=['pyNebula'],

zip_safe=False)
