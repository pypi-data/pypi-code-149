import urwid

def greet_with_urwid():
    txt = urwid.Text(u"Greetings Universe\npress CTRL-c to exit", align='center')
    fill = urwid.Filler(txt, 'middle')
    loop = urwid.MainLoop(fill)
    loop.run()