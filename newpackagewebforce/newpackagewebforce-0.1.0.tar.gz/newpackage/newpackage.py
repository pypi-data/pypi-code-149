"""This is the newpackage.py script."""

import logging

class Newpackage():
    """Newpackage package class."""

    def __init__(self, name=None):
        """Initialize with user-defined parameters."""
        self.name = name

    def use_logger(self):
        logging.warning(f"Youre logged {self.name}")

    def show(self):
        """Run the show function."""
        if self.name is None:
            print('Hello dude i dont know your name')
        else:
            print(f'Hello {self.name} youre cool')

        # Return
        return None
