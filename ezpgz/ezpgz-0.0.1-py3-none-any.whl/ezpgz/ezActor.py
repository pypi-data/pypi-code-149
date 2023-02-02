def ezActor(path, x, y, scale=1, anchor=('center', 'center')):
    import pgzrun
    from pgzero.builtins import Actor, animate, keyboard

    a = Actor(path, anchor=anchor)
    a.x = x
    a.y = y
    a.scale = scale
    return a