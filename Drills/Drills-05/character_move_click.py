from pico2d import *

KPU_WIDTH, KPU_HEIGHT = 1280, 1024


def handle_events():
    global running
    global mx, my
    global cx, cy
    global ex, ey
    global x, y
    global dir
    events = get_events()
    for event in events:
        if event.type == SDL_QUIT:
            running = False
        elif event.type == SDL_MOUSEMOTION:
            mx, my = event.x, KPU_HEIGHT - 1 - event.y
        elif event.type == SDL_MOUSEBUTTONDOWN and event.button == SDL_BUTTON_LEFT:
            cx, cy = event.x - 20, KPU_HEIGHT - 1 - event.y + 20
            ex, ey = x, y
            for i in range(0, 100 + 1, 1):
                clear_canvas()
                kpu_ground.draw(KPU_WIDTH // 2, KPU_HEIGHT // 2)
                arrow.draw(mx, my)
                t = i / 100
                x = (1 - t) * ex + t * cx
                y = (1 - t) * ey + t * cy
                if cx > ex :
                    dir = 100
                else :
                    dir = 0
                character.clip_draw(frame * 100, dir, 100, 100, x, y)
                update_canvas()
        elif event.type == SDL_KEYDOWN and event.key == SDLK_ESCAPE:
            running = False


open_canvas(KPU_WIDTH, KPU_HEIGHT)
kpu_ground = load_image('KPU_GROUND.png')
arrow = load_image('hand_arrow.png')
character = load_image('animation_sheet.png')

running = True
mx, my = KPU_WIDTH // 2, KPU_HEIGHT // 2
cx, cy = KPU_WIDTH // 2, KPU_HEIGHT // 2
ex, ey = KPU_WIDTH // 2, KPU_HEIGHT // 2
x, y = KPU_WIDTH // 2, KPU_HEIGHT // 2
dir = 100
frame = 0
hide_cursor()


while running:
    kpu_ground.draw(KPU_WIDTH // 2, KPU_HEIGHT // 2)
    character.clip_draw(frame * 100, dir, 100, 100, x, y)
    arrow.draw(mx, my)
    update_canvas()
    frame = (frame + 1) % 8

    handle_events()
close_canvas()
