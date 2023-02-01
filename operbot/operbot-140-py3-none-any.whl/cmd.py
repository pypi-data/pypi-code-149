# This file is placed in the Public Domain.


"commands"


from opr.hdl import Command


def __dir__():
    return (
            'cmd',
           )


def cmd(event):
    event.reply(",".join(sorted(Command.cmd)))
