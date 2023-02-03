import json
import setuptools

kwargs = json.loads(
    """
{
    "name": "cdk-cloudformation-generic-database-schema",
    "version": "1.0.0.a7",
    "description": "Uses the Aurora Data API to execute SQL and enforce a schema within a database cluster. Currently only supports Aurora Postgres.",
    "license": "Apache-2.0",
    "url": "https://github.com/iann0036/cfn-types/tree/master/generic-database-schema",
    "long_description_content_type": "text/markdown",
    "author": "Amazon Web Services",
    "bdist_wheel": {
        "universal": true
    },
    "project_urls": {
        "Source": "https://github.com/cdklabs/cdk-cloudformation.git"
    },
    "package_dir": {
        "": "src"
    },
    "packages": [
        "cdk_cloudformation_generic_database_schema",
        "cdk_cloudformation_generic_database_schema._jsii"
    ],
    "package_data": {
        "cdk_cloudformation_generic_database_schema._jsii": [
            "generic-database-schema@1.0.0-alpha.7.jsii.tgz"
        ],
        "cdk_cloudformation_generic_database_schema": [
            "py.typed"
        ]
    },
    "python_requires": "~=3.7",
    "install_requires": [
        "aws-cdk-lib>=2.63.0, <3.0.0",
        "constructs>=10.1.239, <11.0.0",
        "jsii>=1.74.0, <2.0.0",
        "publication>=0.0.3",
        "typeguard~=2.13.3"
    ],
    "classifiers": [
        "Intended Audience :: Developers",
        "Operating System :: OS Independent",
        "Programming Language :: JavaScript",
        "Programming Language :: Python :: 3 :: Only",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
        "Typing :: Typed",
        "License :: OSI Approved"
    ],
    "scripts": []
}
"""
)

with open("README.md", encoding="utf8") as fp:
    kwargs["long_description"] = fp.read()


setuptools.setup(**kwargs)
