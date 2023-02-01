# This file is placed in the Public Domain.


"thread"


import queue
import threading


from .utl import name


def __dir__():
    return (
            'Thread',
            'launch',
           )


__all__ = __dir__()


class Thread(threading.Thread):

    "thread"

    def __init__(self, func, thrname, *args, daemon=True):
        ""
        super().__init__(None, self.run, name, (), {}, daemon=daemon)
        self._exc = None
        self._evt = None
        self._result = None
        self.name = thrname or name(func)
        self.queue = queue.Queue()
        self.queue.put_nowait((func, args))
        self.sleep = None

    def __iter__(self):
        return self

    def __next__(self):
        for k in dir(self):
            yield k

    def join(self, timeout=None):
        "join this thread."
        super().join(timeout)
        return self._result

    def run(self) -> None:
        "run this thread."
        func, args = self.queue.get()
        if args:
            self._evt = args[0]
        self._result = func(*args)


def launch(func, *args, **kwargs):
    "launch a thread."
    thrname = kwargs.get("name", name(func))
    thr = Thread(func, thrname, *args)
    thr.start()
    return thr
