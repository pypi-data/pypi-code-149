import numpy as np


def gameclock_to_wallclock(gameclock):
    """Transforms gameclockclock [s] ot wallclock (min, sec)"""
    sec = str(int(gameclock % 60)).zfill(2)
    min = (gameclock / 60)
    minmod = str(int(min % 60)).zfill(2)
    hour = str(int(np.floor(min / 60))).zfill(2)

    return f"{hour}:{minmod}:{sec}"

