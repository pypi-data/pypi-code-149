import setuptools

setuptools.setup(
    name="rollin-lxd",
    version="0.10.0",
    description="LXD dynamic management based on kivalu",
    long_description="TODO",
    long_description_content_type="text/markdown",
    author="Thomas JOUANNOT",
    author_email="mazerty@gmail.com",
    url="https://zebr0.io/projects/rollin/lxd",
    download_url="https://github.com/zebr0/rollin-lxd",
    packages=["rollin_lxd"],
    scripts=["scripts/rollin-lxd"],
    classifiers=[
        "Development Status :: 4 - Beta",
        "Environment :: Console",
        "Intended Audience :: Developers",
        "Intended Audience :: Information Technology",
        "Intended Audience :: System Administrators",
        "License :: OSI Approved :: MIT License",
        "Natural Language :: English",
        "Operating System :: POSIX",
        "Programming Language :: Python :: 3",
        "Topic :: System"
    ],
    license="MIT",
    install_requires=[
        "kivalu",
        "PyYAML",
        "requests-unixsocket"
    ]
)
