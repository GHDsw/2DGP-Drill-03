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
    for x in range(20, 780, 5):
        drawObject(x, 550)
    pass


def moveRight():
    print('Moving right')
    for y in range(550, 90, -5):
        drawObject(780, y)
    pass


def moveBottom():
    print('Moving bottom')
    for x in range(400, 20, -5):
        drawObject(x, 90)
    pass

def moveBottom2():
    print('Moving bottom2')
    for x in range(780, 400, -5):
        drawObject(x, 90)
    pass

def moveLeft():
    print('Moving left')
    for y in range(90, 550, 5):
        drawObject(20, y)
    pass

def moveRect():
    print('Move Rect')
    x,y=400,90
    moveBottom()
    moveLeft()
    moveTop()
    moveRight()
    moveBottom2()
    pass

def moveRightT():
    for x in range(20, 400, 5):
        drawObject(x, x+90-20)
    pass

def moveLeftT():
    for x in range(400, 780, 5):
        drawObject(x, 890-x-20)
    pass


def moveTri():
    print('Move Tri')
    moveBottom()
    moveRightT()
    moveLeftT()
    moveBottom2()
    pass

def moveCircle():
    r = (600-180)/2
    for deg in range(-90, 360-90):
        x = r * math.cos(math.radians(deg)) + 400
        y = r * math.sin(math.radians(deg)) + 300
        clear_canvas_now()

        drawObject(x, y)
    pass

while True:
    #moveRect()
    #moveTri()
    moveCircle()
    break
    pass

close_canvas()
