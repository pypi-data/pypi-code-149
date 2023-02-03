def go():
    import os
    import pgzrun
    
    os.environ['SDL_VIDEO_WINDOW_POS'] = '1'
    pgzrun.go() # Must be last line
