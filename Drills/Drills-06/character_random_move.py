from pico2d import *
import random

KPU_WIDTH, KPU_HEIGHT = 1280, 1024




def handle_events():
    global running
    global x, y
    global dir
    events = get_events()
    for event in events:
        if event.type == SDL_QUIT:
            running = False
        elif event.type == SDL_KEYDOWN and event.key == SDLK_ESCAPE:
            running = False


def setxy(t, p1, p2, p3, p4):
    global frame
    global x, y
    x = ((-t ** 3 + 2 * t ** 2 - t) * p[p1][0] + (3 * t ** 3 - 5 * t ** 2 + 2) * p[p2][0] + (
            -3 * t ** 3 + 4 * t ** 2 + t) * p[p3][0] + (t ** 3 - t ** 2) * p[p4][0]) / 2
    y = ((-t ** 3 + 2 * t ** 2 - t) * p[p1][1] + (3 * t ** 3 - 5 * t ** 2 + 2) * p[p2][1] + (
            -3 * t ** 3 + 4 * t ** 2 + t) * p[p3][1] + (t ** 3 - t ** 2) * p[p4][1]) / 2
    if p[p2][0] > p[p3][0]:
        dir = 0
    else:
        dir = 100
    draw_xy(x, y, dir)
    frame = (frame + 1) % 8


def draw_curve_4_points():

    # draw p1-p2
    for i in range(0, 100, 2):
        t = i / 100
        setxy(t, 9, 0, 1, 2)

    for i in range(0, 100, 2):
        t = i / 100
        setxy(t, 0, 1, 2, 3)

    for i in range(0, 100, 2):
        t = i / 100
        setxy(t, 1, 2, 3, 4)

    for i in range(0, 100, 2):
        t = i / 100
        setxy(t, 2, 3, 4, 5)

    for i in range(0, 100, 2):
        t = i / 100
        setxy(t, 3, 4, 5, 6)

    for i in range(0, 100, 2):
        t = i / 100
        setxy(t, 4, 5, 6, 7)

    for i in range(0, 100, 2):
        t = i / 100
        setxy(t, 5, 6, 7, 8)

    for i in range(0, 100, 2):
        t = i / 100
        setxy(t, 6, 7, 8, 9)

    for i in range(0, 100, 2):
        t = i / 100
        setxy(t, 7, 8, 9, 0)

    for i in range(0, 100, 2):
        t = i / 100
        setxy(t, 8, 9, 0, 1)



def draw_xy(x, y, dir):
    clear_canvas()
    kpu_ground.draw(KPU_WIDTH // 2, KPU_HEIGHT // 2)
    character.clip_draw(frame * 100, dir, 100, 100, x, y)
    update_canvas()

    delay(0.01)


open_canvas(KPU_WIDTH, KPU_HEIGHT)
kpu_ground = load_image('KPU_GROUND.png')
character = load_image('animation_sheet.png')

p = [(random.randint(0, KPU_WIDTH), random.randint(0, KPU_HEIGHT)) for i in range(10)]

running = True
x, y = KPU_WIDTH // 2, KPU_HEIGHT // 2
dir = 100
frame = 0

hide_cursor()

while running:
    draw_curve_4_points()

    handle_events()
close_canvas()
