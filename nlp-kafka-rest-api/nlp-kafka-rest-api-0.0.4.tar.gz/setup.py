from setuptools import setup

VERSION = '0.0.4'
DESCRIPTION = 'Kafka REST API'
LONG_DESCRIPTION = 'This package is a wrapper for REST API requests to Kafka Proxy.'

setup(
    name="nlp-kafka-rest-api",
    version=VERSION,
    description=DESCRIPTION,
    long_description=LONG_DESCRIPTION,
    author="X251258",
    author_email="X251258@one.merckgroup.com",
    install_requires=['requests'],
    keywords=['kafka', 'rest', 'api', 'batch', 'processing'],
    classifiers=[
        "Development Status :: 2 - Pre-Alpha",
        "Intended Audience :: Developers",
        "Programming Language :: Python :: 3",
    ]
)
