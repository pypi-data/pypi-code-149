import json
import setuptools

kwargs = json.loads(
    """
{
    "name": "cdk-cloudformation-tf-aws-s3bucketobject",
    "version": "1.0.0.a7",
    "description": "Provides a S3 bucket object resource.",
    "license": "Apache-2.0",
    "url": "https://github.com/iann0036/cfn-tf-custom-types/blob/docs/resources/aws/TF-AWS-S3BucketObject/docs/README.md",
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
        "cdk_cloudformation_tf_aws_s3bucketobject",
        "cdk_cloudformation_tf_aws_s3bucketobject._jsii"
    ],
    "package_data": {
        "cdk_cloudformation_tf_aws_s3bucketobject._jsii": [
            "tf-aws-s3bucketobject@1.0.0-alpha.7.jsii.tgz"
        ],
        "cdk_cloudformation_tf_aws_s3bucketobject": [
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
