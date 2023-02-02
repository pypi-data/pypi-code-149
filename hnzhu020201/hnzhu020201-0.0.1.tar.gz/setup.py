import setuptools

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setuptools.setup(
    name="hnzhu020201",
    version="0.0.1",
    author="hnzhu2",
    author_email="1170618497@qq.com",
    description="A small example package",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
     install_requires=[
            'airtest==1.2.6',
            'pyppeteer==0.2.6',
            'artifactory==0.1.17',
            'pixelmatch',
            'paramiko==2.11.0',
            'pandas==1.1.5',
            'poco==0.99.1',
            'pocoui==1.0.87',
            'allure-combine==1.0.6',
            'allure-pytest==2.9.45',
            'allure-python-commons==2.9.45',
            'openpyxl==3.0.10',
    ],
    
    
)