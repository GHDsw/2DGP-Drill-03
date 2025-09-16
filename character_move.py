from pico2d import *

open_canvas()

boy = load_image('character.png')

# fill here
def moveTop():
    pass


def moveRight():
    pass


def moveBottom():
    pass


def moveLeft():
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

        clear_canvas_now()
        boy.draw_now(x,y)
        delay(0.01)
    pass


while True:
    moveCircle()
    moveRect()
    break
    pass

close_canvas()
