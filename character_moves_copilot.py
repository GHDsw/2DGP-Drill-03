from pico2d import *
import math

open_canvas()

boy = load_image('character.png')
grass = load_image('grass.png')

def drawObject(x: float, y: float):
    clear_canvas_now()
    grass.draw_now(400, 30)
    boy.draw_now(x, y)
    delay(0.01)

def moveTop():
    for x in range(20, 780, 5):
        drawObject(x, 550)

def moveRight():
    for y in range(550, 90, -5):
        drawObject(780, y)

def moveBottom():
    for x in range(400, 20, -5):
        drawObject(x, 90)

def moveBottom2():
    for x in range(780, 400, -5):
        drawObject(x, 90)

def moveLeft():
    for y in range(90, 550, 5):
        drawObject(20, y)

def moveRect():
    moveBottom()
    moveLeft()
    moveTop()
    moveRight()
    moveBottom2()

def moveRightT():
    for x in range(20, 400, 5):
        drawObject(x, x+90-20)

def moveLeftT():
    for x in range(400, 780, 5):
        drawObject(x, 890-x-20)

def moveTri():
    moveBottom()
    moveRightT()
    moveLeftT()
    moveBottom2()

def moveCircle():
    r = (600-180)/2
    for deg in range(-90, 360-90):
        x = r * math.cos(math.radians(deg)) + 400
        y = r * math.sin(math.radians(deg)) + 300
        drawObject(x, y)

while True:
    moveRect()
    moveTri()
    moveCircle()

close_canvas()

