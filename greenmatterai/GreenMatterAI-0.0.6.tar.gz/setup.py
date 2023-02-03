import setuptools

setuptools.setup(
    name="GreenMatterAI",
    version="0.0.6",
    author="GreenMatterAI",
    description="GreenMatterAI's package",
    packages=["GreenMatterAI"],
    install_requires=[
        "requests",
        "shortuuid",
        "aws_requests_auth",
        "boto3",
        "pathlib",
        "datetime"
    ]
)
