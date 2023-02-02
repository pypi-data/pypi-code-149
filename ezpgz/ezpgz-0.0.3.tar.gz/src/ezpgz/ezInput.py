def left():
    from pgzero.builtins import keyboard
    if keyboard.left or keyboard.a:
        return True
    else:
        return False

def right():
    from pgzero.builtins import keyboard
    if keyboard.right or keyboard.d:
        return True
    else:
        return False

def up():
    from pgzero.builtins import keyboard
    if keyboard.up or keyboard.w:
        return True
    else:
        return False
    
def down():
    from pgzero.builtins import keyboard
    if keyboard.down or keyboard.s:
        return True
    else:
        return False


