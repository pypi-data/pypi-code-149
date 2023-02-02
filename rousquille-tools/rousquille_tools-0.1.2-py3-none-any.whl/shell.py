import os
import re


def is_in_screen_session() -> bool:
    if re.match(r"screen.*", os.environ["TERM"]):
        return True
    return False
