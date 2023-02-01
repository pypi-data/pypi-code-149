# This file is placed in the Public Domain.
# pylint: disable=W0703


"table"


import os


from .thr import launch


def __dir__():
    return (
            'Bus',
            'Callback',
            'Class',
            'Command',
            'Wd',
            'setwd'
           )


__all__ = __dir__()


class Bus:

    "bus"

    objs = []

    @staticmethod
    def add(obj):
        "add listener."
        if repr(obj) not in [repr(x) for x in Bus.objs]:
            Bus.objs.append(obj)

    @staticmethod
    def announce(txt):
        "announce text."
        for obj in Bus.objs:
            obj.announce(txt)

    @staticmethod
    def byorig(orig):
        "return listener by origin."
        res = None
        for obj in Bus.objs:
            if repr(obj) == orig:
                res = obj
                break
        return res

    @staticmethod
    def say(orig, channel, txt):
        "say text in originating bot's channel."
        bot = Bus.byorig(orig)
        if bot:
            bot.say(channel, txt)


class Callback:

    "callback"

    cbs = {}
    errors = []

    @staticmethod
    def register(typ, cbs):
        "register a callback."
        if typ not in Callback.cbs:
            Callback.cbs[typ] = cbs

    @staticmethod
    def callback(event):
        "run callback on an event."
        func = Callback.cbs.get(event.type, None)
        if not func:
            event.ready()
            return
        event.__thr__ = launch(func, event, name=event.txt)

    @staticmethod
    def dispatch(event):
        "dispatch an event."
        Callback.callback(event)

    @staticmethod
    def get(typ):
        "return callback."
        return Callback.cbs.get(typ, None)


class Command:

    "command"

    cmd = {}
    errors = []

    @staticmethod
    def add(cmd):
        "add command."
        Command.cmd[cmd.__name__] = cmd

    @staticmethod
    def get(cmd):
        "return command."
        return Command.cmd.get(cmd)

    @staticmethod
    def handle(evt):
        "handle an event."
        if not evt.isparsed:
            evt.parse(evt.txt)
        func = Command.get(evt.cmd)
        if func:
            try:
                func(evt)
            except Exception as ex:
                exc = ex.with_traceback(ex.__traceback__)
                Command.errors.append(exc)
                evt.ready()
                return None
            evt.show()
        evt.ready()
        return None

    @staticmethod
    def remove(cmd):
        "remove command."
        del Command.cmd[cmd]


class Class:

    "class"

    cls = {}

    @staticmethod
    def add(clz):
        "add class."
        Class.cls["%s.%s" % (clz.__module__, clz.__name__)] =  clz

    @staticmethod
    def all():
        "all classes."
        return Class.cls.keys()

    @staticmethod
    def full(oname):
        "return full qualified names."
        nme = oname.lower()
        res = []
        for cln in Class.cls:
            if nme == cln.split(".")[-1].lower():
                res.append(cln)
        return res

    @staticmethod
    def get(oname):
        "return class"
        return Class.cls.get(oname, None)

    @staticmethod
    def remove(oname):
        "remove class."
        del Class.cls[oname]


class Wd:

    "workdir"

    workdir = ""

    @staticmethod
    def get():
        "return working directory."
        assert Wd.workdir
        return Wd.workdir

    @staticmethod
    def getpath(path):
        "add path to working directory."
        return os.path.join(Wd.get(), "store", path)

    @staticmethod
    def set(path):
        "set working directory."
        Wd.workdir = path

    @staticmethod
    def storedir():
        "return storage directory."
        return os.path.join(Wd.get(), "store")

    @staticmethod
    def types(oname=None):
        "list full qualified names in storage directory."
        res = []
        path = Wd.storedir()
        if not os.path.exists(path):
            return res
        for fnm in os.listdir(path):
            if oname and oname.lower() not in fnm.split(".")[-1].lower():
                continue
            if fnm not in res:
                res.append(fnm)
        return res


def setwd(wdr):
    "set working directory."
    Wd.set(wdr)
