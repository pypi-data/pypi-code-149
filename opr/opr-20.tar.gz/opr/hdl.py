# This file is placed in the Public Domain.


"handler"


import queue
import threading
import time


from .obj import Class
from .prs import Parsed
from .tbl import Bus, Callback, Command


def __dir__():
    return (
            'Event',
            'Handler',
           )


__all__ = __dir__()



class Event(Parsed):

    "event"

    def __init__(self):
        Parsed.__init__(self)
        self.__ready__ = threading.Event()
        self.__thr__ = None
        self.control = "!"
        self.createtime = time.time()
        self.result = []
        self.type = "event"

    def bot(self):
        "originating bot."
        return Bus.byorig(self.orig)

    def error(self):
        "handle error."

    def done(self, txt=None):
        "flag as finished."
        text = "ok " + (txt or "")
        text = text.rstrip()
        Bus.say(self.orig, self.channel, text)

    def ready(self):
        "event is ready."
        self.__ready__.set()

    def reply(self, txt):
        "add text to result."
        self.result.append(txt)

    def show(self):
        "show result."
        for txt in self.result:
            Bus.say(self.orig, self.channel, txt)

    def wait(self):
        "wait for event to finish."
        if self.__thr__:
            self.__thr__.join()
        self.__ready__.wait()


Class.add(Event)


class Handler(Callback):

    "handler"

    def __init__(self):
        Callback.__init__(self)
        self.queue = queue.Queue()
        self.stopped = threading.Event()
        self.stopped.clear()
        self.register("event", Command.handle)
        Bus.add(self)

    @staticmethod
    def add(cmd):
        "add command."
        Command.add(cmd)

    def announce(self, txt):
        "announce text."
        self.raw(txt)

    @staticmethod
    def handle(event):
        "handle an event."
        Callback.dispatch(event)

    def loop(self):
        "handler's loop."
        while not self.stopped.set():
            self.handle(self.poll())

    def poll(self):
        "return event."
        return self.queue.get()

    def put(self, event):
        "put event to proces."
        self.queue.put_nowait(event)

    def raw(self, txt):
        "raw output to console."

    def restart(self):
        "restart handler."
        self.stop()
        self.start()

    def say(self, channel, txt):
        "say text in channel."
        if not channel:
            self.raw(txt)

    def stop(self):
        "stop handler."
        self.stopped.set()

    def start(self):
        "start handler."
        self.stopped.clear()
        self.loop()
