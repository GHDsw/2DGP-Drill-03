from pico2d import *

open_canvas()

boy = load_image('character.png')

# fill here
def moveTop():
    print('Moving top')
    for x in range(0, 800, 5):
        drawBoy(x,550)
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
    print ("moveRect")
    moveTop()
    moveRight()
    moveBottom()
    moveLeft()
    pass


def moveCircle():
    print ("moveCircle")
    r=200
    for deg in range(0, 360):
        x = r * math.cos(math.radians(deg))+400
        y = r * math.sin(math.radians(deg))+300
        clear_canvas_now()

        drawBoy(x, y)
    pass


def drawBoy(x: float, y: float):
    clear_canvas_now()
    boy.draw_now(x, y)
    delay(0.01)


while True:
    # moveCircle()
    moveRect()
    break
    pass

close_canvas()
