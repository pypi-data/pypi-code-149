#!/usr/bin/env python3

from setuptools import setup


def main() -> None:
    setup(
            name="ODBPlotter",
            version="0.0.1",
            author="Clark Hensley",
            author_email="clarkhensley@duck.com",
            description="TODO",
            url="TODO",
            license="TODO",
            py_modules=["odb"],
            scripts=["bin/odb_plotter.py"],
            package_data={
                "static": ["*"],
                },
            )


if __name__ == "__main__":
    main()
