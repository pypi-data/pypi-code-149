def get_cache():
    global cache
    try: cache
    except: cache = []
    return cache

def append_cache(a):
    cache = get_cache()
    if not a in cache:
        cache += [a]

def clear_cache():
    global cache
    cache = []

def remove_cache(Sprite):
    cache = get_cache()
    if Sprite in cache:
        cache -= Sprite