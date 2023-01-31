import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="cux",
    version="0.2.2",  # Latest version .
    author="r2fscg",
    author_email="r2fscg@gmail.com",
    description="PLACEHOLDER",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/private_repo/yaya",
    packages=setuptools.find_packages(),
    package_data={"cux": ["data/*.txt", "data/*.csv"], },
    entry_points={
        "console_scripts": [
            "oldjql=cux.main:gate",
            "jql=cux.newjql:main",
            "redo=cux.redo:entry",
            "check_intelligence=cux.main:check_intelligence_result",
            "display_it=cux.main:display_intelligence_time_periods",
            "nsqstatus=cux.nsqstatus:cli",
            "eloop=cux.jupytersql:eloop",
            'cuxserve=cux.server:serve'
        ],
    },
    install_requires=["codefast", "func-timeout", "flask", 'arrow', 'joblib', 'numpy', 'pydantic', 'rich', 'sshtunnel',
                      'oss2', 'pyserverless', "redis", "pandas", "pymysql"],
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
)
