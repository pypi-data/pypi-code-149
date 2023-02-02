import pgzrun
import random

WIDTH = 800
HEIGHT = 600

game_over = False
score = 0

background = Actor('water')

player = Actor('p1_front')
player.x = 400
player.y = 300

enemies = []

sounds.sneakingaround.play(-1)

def update():
    global score, game_over

    if game_over:
        return

    score += 1 / 60

    play_walking_sound = False
    if keyboard.up:
        player.y -= 5
        play_walking_sound = True
    if keyboard.down:
        player.y += 5
        play_walking_sound = True
    if keyboard.left:
        player.x -= 5
        play_walking_sound = True
    if keyboard.right:
        player.x += 5
        play_walking_sound = True

    if play_walking_sound:
        if sounds.footsteps.get_num_channels() == 0:
            sounds.footsteps.play()

    if random.randint(0, 60) == 0:
        side = random.randint(1, 4)
        enemy = Actor('worm.png')

        if side == 1:
            enemy.y = random.randint(0, 600)
            enemy.x = 850
            enemy.angle = 0
        elif side == 2:
            enemy.y = random.randint(0, 600)
            enemy.x = -50
            enemy.angle = 180
        elif side == 3:
            enemy.y = 650
            enemy.x = random.randint(0, 800)
            enemy.angle = 270
        elif side == 4:
            enemy.y = -50
            enemy.x = random.randint(0, 800)
            enemy.angle = 90

        enemies.append(enemy)

    for enemy in enemies:
        if enemy.angle == 0:
            enemy.x -= 3
        elif enemy.angle == 180:
            enemy.x += 3
        elif enemy.angle == 270:
            enemy.y -= 3
        elif enemy.angle == 90:
            enemy.y += 3

        if enemy.x < -50 or enemy.x > 850 or enemy.y < -50 or enemy.y > 650:
            enemies.remove(enemy)

    if player.collidelist(enemies) != -1:
        game_over = True

def draw():
    if game_over:
        screen.clear()
        screen.draw.text('Game Over', (350,270), color=(255,255,255), fontsize=30)
        screen.draw.text('Score: ' + str(round(score)), (350,330), color=(255,255,255), fontsize=30)
    else:
        background.draw()
        player.draw()
        for enemy in enemies:
            enemy.draw()
        screen.draw.text('Score: ' + str(round(score)), (15,10), color=(255,255,255), fontsize=30)

pgzrun.go()
