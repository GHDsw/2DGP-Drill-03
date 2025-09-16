from pico2d import *
import math

open_canvas()

boy = load_image('character.png')

def move_rect():
    # 위로 이동
    for x in range(0, 800, 5):
        clear_canvas_now()
        boy.draw_now(x, 550)
        delay(0.01)

    # 오른쪽으로 이동
    for y in range(550, 0, -5):
        clear_canvas_now()
        boy.draw_now(800, y)
        delay(0.01)

    # 아래로 이동
    for x in range(800, 0, -5):
        clear_canvas_now()
        boy.draw_now(x, 0)
        delay(0.01)

    # 왼쪽으로 이동
    for y in range(0, 550, 5):
        clear_canvas_now()
        boy.draw_now(0, y)
        delay(0.01)

def move_circle():
    r = 200  # 반지름
    for deg in range(0, 360):
        x = r * math.cos(math.radians(deg)) + 400
        y = r * math.sin(math.radians(deg)) + 300
        clear_canvas_now()
        boy.draw_now(x, y)
        delay(0.01)

while True:
    move_rect()   # 먼저 사각 운동
    move_circle() # 이어서 원 운동

close_canvas()
