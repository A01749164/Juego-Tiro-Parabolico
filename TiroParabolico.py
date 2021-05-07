"""Cannon, hitting targets with projectiles.

Exercises

1. Keep score by counting target hits.
2. Vary the effect of gravity.
3. Apply gravity to the targets.
4. Change the speed of the ball.

"""

from random import randrange
from turtle import *
from freegames import vector

ball = vector(-200, -200) # La pelota en su posición inicial
speed = vector(0, 0) # La velocidad inicial de la pelota
targets = [] # Lista de los objetivos en pantalla

def tap(x, y):
    """Responde a un click en la pantalla."""
    if not inside(ball):
        # Mueve las coordenadas de la pelota
        ball.x = -199
        ball.y = -199
        # Establece la velocidad de la pelota
        speed.x = (x + 200) / 10
        speed.y = (y + 200) / 10


def inside(xy):
    """Regresa verdadero si la pelota está en la pantalla"""
    return -200 < xy.x < 200 and -200 < xy.y < 200


def draw():
    """Dibuja la pelota y los objetivos"""
    clear()

    # Dibuja todos los objetivos
    for target in targets:
        goto(target.x, target.y)
        dot(20, 'blue')

    # Dibuja la pelota
    if inside(ball):
        goto(ball.x, ball.y)
        dot(6, 'red')

    update()


def move():
    """Mueve la pelota y los objetivos"""
    # Crea los objetivos con una probabilidad de 1:20
    if randrange(20) == 0:
        y = randrange(-150, 150)
        target = vector(200, y)
        targets.append(target)

    # Mueve los objetivos
    for target in targets:
        target.x -= 2 # Velocidad de movimiento

    # Disminuye la velocidad en y de la pelota
    if inside(ball):
        speed.y -= 2 # Crea el efecto de parábola
        ball.move(speed)

    dupe = targets.copy()
    targets.clear()

    for target in dupe:
        if abs(target - ball) > 13:
            targets.append(target)

    draw()

    for target in targets:
        if not inside(target):
            return

    ontimer(move, 50)

setup(420, 420, 370, 0)
hideturtle()
up()
tracer(False)
onscreenclick(tap)
move()
done()