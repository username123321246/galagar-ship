import pgzrun
from random import randint

WIDTH=700
HEIGHT=500

BLUE = (0,0,255)
BLACK = (0,0,0)

enemy = Actor("enemy")
ship = Actor("ship")

ship.pos = (WIDTH/2, HEIGHT - 50)

bullets = []

enemies = []
enemies.append(Actor("enemy"))

speed = 5

score = 0

enemies[-1].x = 10
enemies[-1].y = -100

def draw():
    screen.clear()
    screen.fill(BLUE)
    for bullet in bullets:
        bullet.draw()
    for enemy in enemies:
        enemy.draw()
    ship.draw()
    screen.draw.text(str(score), (1000, 20), fontsize = 30, color = "white")

def on_key_down(key):
        if key == keys.SPACE:
            bullets.append(Actor("bullet"))
            # The last bullet added set its position
            bullets[-1].x = ship.x
            bullets[-1].y = ship.y - 40


def update():
    global score
    if keyboard.left:
          ship.x -= 5
          if ship.x <= 0:
               ship.x = 0
    
    elif keyboard.right:
        ship.x += 5
        if ship.x >= WIDTH:
            ship.x = WIDTH
    
    for bullet in bullets:
        if bullet.y <= 0:
            bullets.remove(bullet)

        else:
            bullet.y -= 10

    for enemy in enemies:
         enemy.y += 5
         if enemy.y >= HEIGHT:
            enemy.x = randint(10, 500)
            enemy.y = -100
        
    for bullet in bullets:
         if enemy.colliderect(bullet):
            score += 10
            bullets.remove(bullet)
            enemies.remove(enemy)



pgzrun.go()







