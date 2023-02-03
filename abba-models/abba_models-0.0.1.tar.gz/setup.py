import setuptools

setuptools.setup(
    name="abba_models",
    version="0.0.1",
    license="MIT",
    author="ABBA",
    author_email="",
    description="abba model",
    url="",
    packages=setuptools.find_packages(),
    package_data={"":["**/*"]},
    install_requires=open("requirements.txt", "r").read().splitlines(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent"
    ]

)