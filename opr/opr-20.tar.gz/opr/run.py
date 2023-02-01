# This file is placed in the Public Domain.
# pylint: disable=W0201


"runtime"


from .hdl import Event, Handler
from .obj import Default, update
from .prs import Parsed


def __dir__():
    return (
            "Cfg",
            "boot",
            "command",
            "parse"
           )


__all__ = __dir__()


#:
Cfg = Default()
Cfg.prs = Parsed()


def boot(txt):
    "parse command line."
    prs = parse(txt)
    if "c" in prs.opts:
        Cfg.console = True
    if "d" in prs.opts:
        Cfg.daemon= True
    if "v" in prs.opts:
        Cfg.verbose = True
    if "w" in prs.opts:
        Cfg.wait = True
    if "x" in prs.opts:
        Cfg.exec = True
    update(Cfg.prs, prs)
    update(Cfg, prs.sets)


def command(txt, cli=None, event=None):
    "execute a command."
    cli = cli or Handler()
    evt = (event() if event else Event())
    evt.parse(txt)
    evt.orig = repr(cli)
    cli.handle(evt)
    evt.wait()
    return evt


def parse(txt):
    "parse text."
    prs = Parsed()
    prs.parse(txt)
    update(Cfg.prs, prs)
    return prs
