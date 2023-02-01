# This file is placed in the Public Domain.


"logging"


import time


from opr.dbs import find, fntime
from opr.jsn import save
from opr.obj import Class, Object
from opr.utl import elapsed


def __dir__():
    return (
            'Log',
            'log',
           )


class Log(Object):

    def __init__(self):
        Object.__init__(self)
        self.txt = ""


Class.add(Log)


def log(event):
    if not event.rest:
        nmr = 0
        for obj in find("log"):
            event.reply("%s %s %s" % (
                                      nmr,
                                      obj.txt,
                                      elapsed(time.time() - fntime(obj.__fnm__)))
                                     )
            nmr += 1
        if not nmr:
            event.reply("log <txt>")
        return
    obj = Log()
    obj.txt = event.rest
    save(obj)
    event.done()
