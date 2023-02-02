import argparse
import os
import re
import sys


def is_pep8_compliant(file_name):
    # PEP 8 file naming conventions state that module names should be lowercase,
    # and may contain underscores and numbers
    return re.match(r"^[a-z0-9_]+\.py$", file_name) is not None


def check_directory(directory):
    # Check if the directory exists
    if not os.path.exists(directory):
        raise Exception(f"Error: The directory '{directory}' does not exist.")

    errors = []
    for root, dirs, files in os.walk(directory):
        for file_name in files:
            full_path = os.path.join(root, file_name)
            ignore = file_name.endswith(".py") and not file_name.startswith(
                "__"
            )
            if ignore and not is_pep8_compliant(file_name):
                errors.append(
                    f"Error: {full_path} does not follow PEP 8 file naming conventions."
                )

    if errors:
        raise Exception("\n".join(errors))


def main():
    parser = argparse.ArgumentParser(
        description='Check if .py files in the specified directories follow PEP 8 file naming conventions, excluding files starting with "__".'
    )
    parser.add_argument(
        "directories",
        metavar="dir",
        type=str,
        nargs="+",
        help="the directories to check",
    )
    args = parser.parse_args()

    input_directories = args.directories
    for directory in input_directories:
        try:
            check_directory(directory)
        except Exception as e:
            print(e)
            sys.exit(1)


if __name__ == "__main__":
    main()
