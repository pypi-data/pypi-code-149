from setuptools import setup


setup(
    name="cohesive-marketplace-server-sdk-python",
    version="1.0.2",
    description="Python bindings for the Cohesive Marketplace API",
    author="Cohesive",
    author_email="contact@cohesive.so",
    url="https://github.com/getcohesive/marketplace-server-sdk-python",
    license="MIT",
    keywords="cohesive api marketplace saas",
    packages=['cohesive', 'cohesive.api_resources'],
    install_requires=[
        'requests >= 2.28.2',
        'PyJWT >= 2.6.0',
    ],
    python_requires=">=3.7",
    project_urls={
        "Source Code": "https://github.com/getcohesive/marketplace-server-sdk-python",
    },
    classifiers=[
        "Development Status :: 5 - Production/Stable",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
        "Programming Language :: Python",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
        "Programming Language :: Python :: Implementation :: PyPy",
        "Topic :: Software Development :: Libraries :: Python Modules",
    ],
    setup_requires=["wheel"],
)