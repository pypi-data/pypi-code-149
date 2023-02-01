# This file is placed in the Public Domain.


"utility"


import getpass
import os
import pathlib
import pwd
import time
import types


def __dir__():
    return (
            "cdir",
            "elapsed",
            "locked",
            "name",
            "privileges",
            "spl",
            "wait"
           )


__all__ = __dir__()


def cdir(path):
    "create directory."
    pth = pathlib.Path(path)
    if path.split(os.sep)[-1].count(":") == 2:
        pth = pth.parent
    os.makedirs(pth, exist_ok=True)


def elapsed(seconds, short=True):
    "return time delta."
    txt = ""
    nsec = float(seconds)
    if nsec < 1:
        return f"{nsec:.4f}s"
    year = 365*24*60*60
    week = 7*24*60*60
    nday = 24*60*60
    hour = 60*60
    minute = 60
    years = int(nsec/year)
    nsec -= years*year
    weeks = int(nsec/week)
    nsec -= weeks*week
    nrdays = int(nsec/nday)
    nsec -= nrdays*nday
    hours = int(nsec/hour)
    nsec -= hours*hour
    minutes = int(nsec/minute)
    nsec -= int(minute*minutes)
    sec = int(nsec)
    if years:
        txt += "%sy" % years
    if weeks:
        nrdays += weeks * 7
    if nrdays:
        txt += "%sd" % nrdays
    if years and short and txt:
        return txt.strip()
    if hours:
        txt += "%sh" % hours
    if minutes:
        txt += "%sm" % minutes
    if sec:
        txt += "%ss" % sec
    else:
        txt += "0s"
    txt = txt.strip()
    return txt


def locked(lock):

    "locked decorator."

    def lockeddec(func, *args, **kwargs):

        if args or kwargs:
            locked.noargs = True

        def lockedfunc(*args, **kwargs):
            lock.acquire()
            res = None
            try:
                res = func(*args, **kwargs)
            finally:
                lock.release()
            return res

        lockedfunc.__wrapped__ = func
        lockedfunc.__doc__ = func.__doc__
        return lockedfunc

    return lockeddec


def name(obj):
    "return full qualified name of an object."
    typ = type(obj)
    if isinstance(typ, types.ModuleType):
        return obj.__name__
    if "__self__" in dir(obj):
        return "%s.%s" % (obj.__self__.__class__.__name__, obj.__name__)
    if "__class__" in dir(obj) and "__name__" in dir(obj):
        return "%s.%s" % (obj.__class__.__name__, obj.__name__)
    if "__class__" in dir(obj):
        return obj.__class__.__name__
    if "__name__" in dir(obj):
        return "%s.%s" % (obj.__class__.__name__, obj.__name__)
    return None


def privileges(username):
    "set privileges."
    if os.getuid() != 0:
        return
    try:
        pwnam = pwd.getpwnam(username)
    except KeyError:
        username = getpass.getuser()
        pwnam = pwd.getpwnam(username)
    os.setgroups([])
    os.setgid(pwnam.pw_gid)
    os.setuid(pwnam.pw_uid)


def spl(txt):
    "create list from comma seperated string."
    try:
        res = txt.split(",")
    except (TypeError, ValueError):
        res = txt
    return [x for x in res if x]


def wait(func=None):
    "wait forever."
    while 1:
        time.sleep(1.0)
        if func:
            func()
