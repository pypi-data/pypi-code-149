# This file is placed in the Public Domain.


"scanner"


import inspect
import os
import sys


from .obj import Object
from .tbl import Class, Command
from .thr import launch
from .utl import spl


def __dir__():
    return (
            "scan",
            "scancls",
            "scancmd",
            "scanpkg",
            "scandir"
           )


__all__ = __dir__()


def include(name, namelist):
    "seen if name is in namelist."
    for nme in namelist:
        if nme in name:
            return True
    return False


def listmod(path):
    "list module names from files in directory."
    res = []
    if not os.path.exists(path):
        return res
    for fnm in os.listdir(path):
        if fnm.endswith("~") or fnm.startswith("__"):
            continue
        res.append(fnm.split(os.sep)[-1][:-3])
    return res


def scan(mod):
    "scan a module for classes and commands."
    scancls(mod)
    scancmd(mod)


def scancls(mod):
    "scan a module for classes."
    for key, obj in inspect.getmembers(mod, inspect.isclass):
        if key.startswith("cb"):
            continue
        if issubclass(obj, Object):
            Class.add(obj)


def scancmd(mod):
    "scan a module for commands."
    for key, cmd in inspect.getmembers(mod, inspect.isfunction):
        if key.startswith("cb"):
            continue
        names = cmd.__code__.co_varnames
        if "event" in names:
            Command.add(cmd)


def scandir(path, pname=None, enable=None,  disable=None, init=None):
    "scan modules in a directory."
    res = []
    thrs = []
    if pname is None:
        pname = path.split(os.sep)[-1]
    for modname in listmod(path):
        skip = False
        if not modname:
            skip = True
        if disable and include(modname, spl(disable)):
            continue
        if enable and not include(modname, spl(enable)):
            skip = True
        if skip:
            continue
        mname = "%s.%s" % (pname, modname)
        mod = sys.modules.get(mname, None)
        if mod:
            scan(mod)
            if init and "init" in dir(mod):
                thrs.append(launch(mod.init))
            res.append(mod)
    for thr in thrs:
        thr.join()
    return res


def scanpkg(pkg, enable=None, disable=None, init=False):
    "scan a packages modules."
    path = pkg.__path__[0]
    name = pkg.__name__
    return scandir(path, name, enable, disable, init)
