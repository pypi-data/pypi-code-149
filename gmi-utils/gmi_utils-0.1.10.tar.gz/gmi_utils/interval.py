from threading import Event, Thread
from typing import Callable


def call_repeatedly(interval: float, func: Callable[..., any], *args):
    """
    Calls func(*args) every timeout second.
    :param interval: calling interval in seconds
    :param func: function to be called
    :param args: args for func to be called with
    :return: function, that stops calling func(*args) repeatedly
    """

    stopped = Event()

    def loop():
        # the first call is in `interval` secs
        while not stopped.wait(interval):
            func(*args)

    Thread(target=loop).start()
    return stopped.set
