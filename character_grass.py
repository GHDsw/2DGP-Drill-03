from pico2d import *
import math

open_canvas()

grass = load_image('grass.png')
character = load_image('character.png')

x=400
y=90

cx = 400
cy = (600-180)/2+90
r = (600-180)/2

while True:
    # 사각형 경로
    while True:
        clear_canvas_now()
        grass.draw_now(400, 30)
        character.draw_now(x, y)
        if x == 780:
            y += 2
        elif x == 20:
            y -= 2
        if y <= 90:
            x += 2
        elif y >= 550:
            x -= 2
        delay(0.001)
        if x == 400 and y == 90:
            break

    # 원 경로
    theta = -math.pi / 2
    while True:
        x = cx + r * math.cos(theta)
        y = cy + r * math.sin(theta)
        clear_canvas_now()
        grass.draw_now(400, 30)
        character.draw_now(x, y)
        theta -= 0.05
        delay(0.01)
        if theta <= -math.pi * 2.5:
            break
    x = 400
    y = 90

close_canvas()
