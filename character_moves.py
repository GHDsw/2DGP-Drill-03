from pico2d import *

open_canvas()

boy = load_image('character.png')
grass = load_image('grass.png')

def drawObject(x: float, y: float):
    clear_canvas_now()
    grass.draw_now(400, 30)
    boy.draw_now(x, y)
    delay(0.01)

def moveTop():
    print('Moving top')
    drawObject(400, 90)
    pass


def moveRight():
    print('Moving right')
    pass


def moveBottom():
    print('Moving bottom')
    pass


def moveLeft():
    print('Moving left')
    pass

def moveRect():
    print('Move Rect')
    moveTop()
    moveRight()
    moveBottom()
    moveLeft()
    pass

def moveTri():
    print('Move Tri')
    pass

def moveCircle():
    print('Move Circle')
    pass

while True:
    moveCircle()
    moveTri()
    moveRect()
    break
    pass

close_canvas()
