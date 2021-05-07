# Código modificado por:
# Autor: Erick Hernández Silva
# Autor: Jeovani Hernández Bastida

# Se importan las librerias a usar
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

    # Copia los objetivos y los borra 
    dupe = targets.copy()
    targets.clear()

    # Dibuja los objetivos que no han sido tocados por la pelota
    for target in dupe:
        if abs(target - ball) > 13:
            targets.append(target)

    draw()

    # Si un objetivo se sale de la pantalla lo regresa 
    for target in targets:
        if not inside(target):
            target.x = 200

    ontimer(move, 50) # Llama al método move cada 50ms

setup(420, 420, 370, 0)     # Dibuja el canvas
hideturtle()    # Desaparece la tortuga
up()    # Levanta la pluma
tracer(False)   # Quita la animación de dibujo
onscreenclick(tap)  # Escucha el click en la pantalla
move()  # Llama por primera vez al método move
done()