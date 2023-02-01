# This file is placed in the Public Domain.


"object"


import datetime
import os
import uuid


from .tbl import Class


def __dir__():
    return (
            'Default',
            'Object',
            'edit',
            'fmt',
            'items',
            'keys',
            'kind',
            'update',
            'values',
           )


__all__ = __dir__()


class Object:


    "object"

    __slots__ = ("__dict__", "__fnm__")


    def __init__(self, *args, **kwargs):
        object.__init__(self)
        self.__fnm__ = os.path.join(
            kind(self),
            str(uuid.uuid4().hex),
            os.sep.join(str(datetime.datetime.now()).split()),
        )
        if args:
            val = args[0]
            if isinstance(val, list):
                update(self, dict(val))
            elif isinstance(val, zip):
                update(self, dict(val))
            elif isinstance(val, dict):
                update(self, val)
            elif isinstance(val, Object):
                update(self, vars(val))
        if kwargs:
            self.__dict__.update(kwargs)

    def __delitem__(self, key):
        self.__dict__.__delitem__(key)

    def __getitem__(self, key):
        self.__dict__.__getitem__(key)

    def __iter__(self):
        return iter(self.__dict__)

    def __len__(self):
        return len(self.__dict__)

    def __str__(self):
        return str(self. __dict__)

    def __setitem__(self, key, value):
        self.__dict__.__setitem__(key, value)


Class.add(Object)


class Default(Object):

    "default"

    __slots__ = ("__default__",)

    def __init__(self):
        Object.__init__(self)
        self.__default__ = ""

    def __getattr__(self, key):
        return self.__dict__.get(key, self.__default__)

    def __setdefault__(self, default):
        self.__default__ = default


Class.add(Default)


def edit(obj, setter):
    "change a object's attributes."
    for key, value in items(setter):
        setattr(obj, key, value)


def fmt(obj, args="", skip="", plain=False):
    "format an object into a printable string."
    res = []
    keyz = []
    if "," in args:
        keyz = args.split(",")
    if not keyz:
        keyz = keys(obj)
    for key in keyz:
        if key.startswith("_"):
            continue
        if skip:
            skips = skip.split(",")
            if key in skips:
                continue
        value = getattr(obj, key, None)
        if not value:
            continue
        if " object at " in str(value):
            continue
        txt = ""
        if plain:
            value = str(value)
        if isinstance(value, str) and len(value.split()) >= 2:
            txt = '%s="%s"' % (key, value)
        else:
            txt = '%s=%s' % (key, value)
        res.append(txt)
    txt = " ".join(res)
    return txt.strip()


def items(obj):
    "return key/attribute pairs of an object."
    if isinstance(obj, type({})):
        return obj.items()
    return obj.__dict__.items()


def keys(obj):
    "return keys of an object."
    return obj.__dict__.keys()


def kind(obj):
    "show what type an object is."
    kin = str(type(obj)).split()[-1][1:-2]
    if kin == "type":
        kin = obj.__name__
    return kin


def update(obj, data):
    "update attributs on an object."
    for key, value in items(data):
        setattr(obj, key, value)


def values(obj):
    "return values of an object."
    return obj.__dict__.values()
