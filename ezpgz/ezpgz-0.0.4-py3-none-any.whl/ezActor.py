def Actor(path, x, y, scale=1, anchor=('center', 'center')):
    import pgzrun
    from pgzero.builtins import Actor, animate, keyboard
    from . import dataCache

    a = Actor(path, anchor=anchor)
    a.x = x
    a.y = y
    a.scale = scale
    dataCache.append_cache(a)
    return a

def drawActors():
    from pgzero.builtins import Actor, animate, keyboard
    from . import dataCache

    cache = dataCache.get_cache()
    for Sprite in cache:
        Sprite.draw()
    return dataCache.get_cache()
        
