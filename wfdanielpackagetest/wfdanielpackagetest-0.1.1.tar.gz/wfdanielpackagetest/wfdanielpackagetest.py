"""This is the relevantpackage.py script."""

# Import libraries
import os
import logging


class Wfdanielpackagetest():
    """Relevant package class."""

    def __init__(self, message=None):
        self.message = message

    def show(self):
        """Run the show function."""
        if self.message is None:
            print('Hello dude')
        else:
            print(f'Hello {self.message} youre cool')

        # Return
        return None
    
    def use_logger(self):
        logging.warning(f"Youre logged {self.message}")
