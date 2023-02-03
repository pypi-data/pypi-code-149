"""Top-level package for WhenDone."""
from whendone.whendone import WhenDone


__author__ = """Sabri Barac"""
__email__ = 'sabribarac@gmail.com'
__version__ = '1.0.1'


__doc__ = """
================

Description
----------------
WhenDone is a Python package created to notify you through Telegram and/or Slack
when your function is done! Usually usefull for when you're training big ML/DL models.

Example
-------
# Import library
from whendone import WhenDone

# Initialize
notifier = WhenDone(telegram_token="XXXX", slack_token="XXXX")
# If you added a slack token, you need to obtain the ID of a chat and add it.
notifier.addSlackChatID('123456')

# Add the notifier as a decorator
notifier.whendone
def Test():
    print('Hello world')


"""