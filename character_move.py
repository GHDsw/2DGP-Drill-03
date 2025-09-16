from pico2d import *

open_canvas()

boy = load_image('character.png')

# fill here
def moveRect():
    print ("moveRect")
    pass


def moveCircle():
    print ("moveCircle")
    clear_canvas_now()
    boy.draw_now(400,300)
    delay(0.1)
    pass


while True:
    moveCircle()
    moveRect()
    break
    pass

close_canvas()
