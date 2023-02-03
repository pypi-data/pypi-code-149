import pgzrun
import random
import ezpgz
import os

WIDTH, HEIGHT = 800, 600

ship = ezpgz.Actor('playership1_blue', 370, 550)
gem = ezpgz.Actor('gemgreen', random.randint(20, 780), 0)

score = 0
game_over = False

def on_mouse_move(pos, rel, buttons):
    ship.x = pos[0]

def update():
    global score, game_over

    if ezpgz.left(): ship.x -= 5
    if ezpgz.right(): ship.x += 5
        

    gem.y += 4 + (score / 5)
    if gem.y > 600:
        game_over = True
    if gem.colliderect(ship):
        gem.x = random.randint(20, 780)
        gem.y = 0
        score = score + 1

def draw():
    screen.fill((80,0,70))
    if game_over:
        screen.draw.text('Game Over', (360, 300), color=(255,255,255), fontsize=60)
        screen.draw.text('Score: ' + str(score), (360, 350), color=(255,255,255), fontsize=60)
    else:
        ezpgz.drawActors()
        screen.draw.text('Score: ' + str(score), (15,10), color=(255,255,255), fontsize=30)

ezpgz.go() # Must be last line