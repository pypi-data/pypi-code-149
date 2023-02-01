"""This is the relevantpackage.py script."""

# Import libraries
import os

class Wfdanielpackagetest():
    """Relevant package class."""

    def __init__(self, message=None):
        """Initialize with user-defined parameters."""
        self.message = message

    def show(self):
        """Run the show function."""
        if self.message is None:
            print('Hello dude')
        else:
            print(f'Hello {self.message} youre cool')

        # Return
        return None
