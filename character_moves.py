from pico2d import *

open_canvas()

def moveTop():
    print('Moving top')
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

def moveCircle():
    print('Move Circle')
    pass

while True:
    moveCircle()
    moveRect()
    break
    pass

close_canvas()
