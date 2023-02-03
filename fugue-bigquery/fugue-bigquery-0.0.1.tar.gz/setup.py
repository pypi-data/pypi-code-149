from setuptools import setup, find_packages
from fugue_bigquery_version import __version__


with open("README.md") as f:
    LONG_DESCRIPTION = f.read()

setup(
    name="fugue-bigquery",
    version=__version__,
    packages=find_packages(),
    description="Fugue BigQuery integration",
    long_description=LONG_DESCRIPTION,
    long_description_content_type="text/markdown",
    license="Apache-2.0",
    author="Han Wang",
    author_email="goodwanghan@gmail.com",
    keywords="fugue bigquery sql",
    url="http://github.com/fugue-project/fugue-bigquery",
    install_requires=[
        "fugue[ibis]==0.8.1.dev3",
        "fs-gcsfs",
        "pandas-gbq",
        "google-auth",
        "ibis-framework[bigquery]",
    ],
    extras_require={
        "ray": ["fugue[ray]==0.8.1.dev3"],
    },
    classifiers=[
        # "3 - Alpha", "4 - Beta" or "5 - Production/Stable"
        "Development Status :: 3 - Alpha",
        "Intended Audience :: Developers",
        "Topic :: Software Development :: Libraries :: Python Modules",
        "License :: OSI Approved :: Apache Software License",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
        "Programming Language :: Python :: 3 :: Only",
    ],
    python_requires=">=3.8",
    entry_points={
        "fugue.plugins": [
            "bigquery = fugue_bigquery.registry",
            "bigquery_ray = fugue_bigquery.ray_execution_engine[ray]",
            "why = fugue_bigquery.whylogs",
        ],
        "ibis.backends": ["fugue_trino = fugue_trino.ibis_trino"],
    },
)
