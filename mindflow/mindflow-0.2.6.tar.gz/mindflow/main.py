"""
Main
"""

from mindflow.app.app import API
from mindflow.cli.run import cli


def main():
    """
    This is the main function.
    """
    if __name__ == "mindflow.main":
        cli()
    
    api = API()
    api.app.run()

