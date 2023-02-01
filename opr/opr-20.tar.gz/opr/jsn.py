# This file is placed in the Public Domain.


"json"


import datetime
import json
import os
import _thread


from .obj import Object, update
from .tbl import Wd
from .utl import cdir, locked


def __dir__():
    return (
            "ObjectDecoder",
            "ObjectEncoder",
            "dump",
            "dumps",
            "load",
            "loads",
            "save",
            "write"
           )


__all__ = __dir__()


disklock = _thread.allocate_lock()


class ObjectDecoder(json.JSONDecoder):

    "decoder"

    def  __init__(self, *args, **kwargs):
        json.JSONDecoder.__init__(self, *args, **kwargs)

    def decode(self, s, _w=None):
        "decode string"
        value = json.loads(s)
        return Object(value)

    def raw_decode(self, s, *args, **kwargs):
        "raw decode string."
        return json.JSONDecoder.raw_decode(self, s, *args, **kwargs)


class ObjectEncoder(json.JSONEncoder):

    "encoder"

    def  __init__(self, *args, **kwargs):
        json.JSONEncoder.__init__(self, *args, **kwargs)

    def encode(self, o):
        "encode object."
        return json.JSONEncoder.encode(self, o)

    def default(self, o):
        "default conversion."
        if isinstance(o, dict):
            return o.items()
        if isinstance(o, Object):
            return vars(o)
        if isinstance(o, list):
            return iter(o)
        if isinstance(o,
                      (type(str), type(True), type(False),
                       type(int), type(float))
                     ):
            return o
        try:
            return json.JSONEncoder.default(self, o)
        except TypeError:
            return str(o)

    def iterencode(self, o, *args, **kwargs):
        "iter encode an object."
        return json.JSONEncoder.iterencode(self, o, *args, **kwargs)



@locked(disklock)
def dump(obj, opath):
    "dump object to file at opath."
    cdir(opath)
    with open(opath, "w", encoding="utf-8") as ofile:
        json.dump(
            obj.__dict__, ofile, cls=ObjectEncoder, indent=4, sort_keys=True
        )
    return opath


def dumps(obj):
    "dump string an object,"
    return json.dumps(obj, cls=ObjectEncoder)


@locked(disklock)
def load(obj, opath):
    "load object from path."
    splitted = opath.split(os.sep)
    fnm = os.sep.join(splitted[-4:])
    lpath = os.path.join(Wd.workdir, "store", fnm)
    if os.path.exists(lpath):
        with open(lpath, "r", encoding="utf-8") as ofile:
            res = json.load(ofile, cls=ObjectDecoder)
            update(obj, res)
    obj.__fnm__ = fnm


def loads(jss):
    "load object from string."
    return json.loads(jss, cls=ObjectDecoder)


def save(obj):
    "save object."
    prv = os.sep.join(obj.__fnm__.split(os.sep)[:2])
    obj.__fnm__ = os.path.join(prv, os.sep.join(str(datetime.datetime.now()).split()))
    opath = Wd.getpath(obj.__fnm__)
    dump(obj, opath)
    return obj.__fnm__


def write(obj):
    "write object."
    opath = Wd.getpath(obj.__fnm__)
    dump(obj, opath)
    return obj.__fnm__
