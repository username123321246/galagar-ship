import pgzrun
from random import randint

WIDTH=600
HEIGHT=500

BLUE = (0,0,255)
BLACK = (0,0,0)

enemy = Actor("enemy")
ship = Actor("ship")

ship.pos = (WIDTH/2, HEIGHT - 50)

bullets = []

enemies = []

speed = 5

score = 0


def draw():
    screen.clear()
    screen.fill(BLUE)
    for bullet in bullets:
        bullet.draw()
    
    ship.draw()








pgzrun.go()







