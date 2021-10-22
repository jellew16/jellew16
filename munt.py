from pgzero import keyboard
from pgzero.clock import Clock
from pgzero.screen import Screen
import pgzrun
from random import randint

width = 400
height = 400
score = 0
game_over = False

vos = Actor('fox')
vos.pos = 100, 100

munt = Actor('coin')
munt.pos = 200, 200

def draw():
    screen.fill('green')
    vos.draw()
    munt.draw()
    screen.draw.text('score: ' + str(score), color='black', topleft=(10, 10))

    if game_over:
        Screen.fill('pink')
        screen.draw.text('Eindscore: ' + str(score), topleft=(10, 10), fontsize=60)

def plaats_munt():
    munt.x = randint(20, (width - 20))
    munt.y = randint(20, (height - 20))

def tijd_om():
    global game_over
    game_over = True

def update():
    global score

    if keyboard.left:
        vos.x = vos.x - 4
    elif keyboard.right:
        vos.x = vos.x + 4
    elif keyboard.up:
        vos.y = vos.y - 4
    elif keyboard.down:
        vos.y = vos.y + 4
    
    munt_verzameld = vos.colliderect(munt)

    if munt_verzameld:
        score = score + 10
        plaats_munt()

clock.schedule(tijd_om, 15.0)
plaats_munt()

pgzrun.go()