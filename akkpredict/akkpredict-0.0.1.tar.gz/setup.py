try:
    from setuptools import setup, find_packages
except ImportError:
    from distutils.core import setup, find_packages

setup(
    name='akkpredict',
    packages=find_packages(),
    include_package_data=True,
    platforms='any',
    version='0.0.1',
    description='A package for predicting buy and sell signals',
    license='MIT',
    author='Nicolus Rotich',
    author_email='nicholas.rotich@gmail.com',
    install_requires=[
    	"setuptools>=58.1.0",
        "aiohttp>=3.8.1",
        "requests>=2.27.1",
        "fire"
    ],
    url='https://nkrtech.com',
    download_url='https://github.com/moinonin/akkpredict/archive/refs/heads/main.zip',
    classifiers=[
        'License :: OSI Approved :: MIT License',
    ],
)
