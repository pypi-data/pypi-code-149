# This file is placed in the Public Domain.


"database"


import os
import time


from opr.jsn import load
from opr.obj import Object, items, kind, update
from opr.tbl import Class, Wd


def __dir__():
    return (
            'Db',
            'find',
            'last',
            'match',
           )


class Db:

    "database"

    @staticmethod
    def find(otp, selector=None, index=None, timed=None, deleted=True):
        "locate objects."
        if selector is None:
            selector = {}
        nmr = -1
        res = []
        for fnm in fns(otp, timed):
            obj = hook(fnm)
            if deleted and "__deleted__" in obj and obj.__deleted__:
                continue
            if selector and not search(obj, selector):
                continue
            nmr += 1
            if index is not None and nmr != index:
                continue
            res.append(obj)
        return res

    @staticmethod
    def last(otp, selector=None, index=None, timed=None):
        "last object of a type."
        res =  sorted(Db.find(otp, selector, index, timed), key=lambda x: fntime(x.__fnm__))
        if res:
            return res[-1]
        return None


def fnclass(path):
    "return full qualified name in a path."
    try:
        _rest, *pth = path.split("store")
        splitted = pth[0].split(os.sep)
        return splitted[1]
    except ValueError:
        pass
    return None


def fns(otp, timed=None):
    "return filenames"
    if not otp:
        return []
    assert Wd.workdir
    path = os.path.join(Wd.workdir, "store", otp) + os.sep
    res = []
    dname = ""
    for rootdir, dirs, _files in os.walk(path, topdown=False):
        if dirs:
            dname = sorted(dirs)[-1]
            if dname.count("-") == 2:
                ddd = os.path.join(rootdir, dname)
                fls = sorted(os.listdir(ddd))
                if fls:
                    path2 = os.path.join(ddd, fls[-1])
                    if (
                        timed
                        and "from" in timed
                        and timed["from"]
                        and fntime(path2) < timed["from"]
                    ):
                        continue
                    if timed and timed.to and fntime(path2) > timed.to:
                        continue
                    res.append(path2)
    return sorted(res)


def fntime(daystr):
    "filename time"
    daystr = daystr.replace("_", ":")
    datestr = " ".join(daystr.split(os.sep)[-2:])
    if "." in datestr:
        datestr, rest = datestr.rsplit(".", 1)
    else:
        rest = ""
    tme = time.mktime(time.strptime(datestr, "%Y-%m-%d %H:%M:%S"))
    if rest:
        tme += float("." + rest)
    else:
        tme = 0
    return tme


def hook(path):
    "construct from path."
    cname = fnclass(path)
    cls = Class.get(cname)
    if cls:
        obj = cls()
    else:
        obj = Object()
    load(obj, path)
    return obj


def find(otp, selector=None, index=None, timed=None, deleted=True):
    "locate objects."
    names = Class.full(otp)
    if not names:
        names = Wd.types(otp)
    result = []
    for nme in names:
        res = Db.find(nme, selector, index, timed, deleted)
        result.extend(res)
    return sorted(result, key=lambda x: fntime(x.__fnm__))


def last(obj, selector=None):
    "last object of a type."
    if selector is None:
        selector = {}
    ooo = Db.last(kind(obj), selector)
    if ooo:
        update(obj, ooo)
        obj.__fnm__ = ooo.__fnm__


def match(otp, selector=None):
    "last matching object."
    names = Class.full(otp)
    if not names:
        names = Wd.types(otp)
    for nme in names:
        for item in Db.last(nme, selector):
            return item
    return None


def search(obj, selector):
    "see if object matches."
    res = False
    select = Object(selector)
    for key, value in items(select):
        try:
            val = getattr(obj, key)
        except AttributeError:
            continue
        if str(value) in str(val):
            res = True
            break
    return res
