from pico2d import *

KPU_WIDTH, KPU_HEIGHT = 1280, 1024

def handle_events():
    global running
    global x, y
    global cx, cy
    global ex, ey
    events = get_events()
    for event in events:
        if event.type == SDL_QUIT:
            running = False
        elif event.type == SDL_MOUSEMOTION:
            x, y = event.x, KPU_HEIGHT - 1 - event.y
        elif event.type == SDL_MOUSEBUTTONDOWN and event.button == SDL_BUTTON_LEFT:
            #char_move()
            cx, cy = event.x, event.y
        elif event.type == SDL_MOUSEBUTTONUP:
            #char_move()
            #cx, cy = event.x, event.y
            pass
        elif event.type == SDL_KEYDOWN and event.key == SDLK_ESCAPE:
            running = False

#def char_move(p1, p2):
 #   draw_big_point(p1)
  #  draw_big_point(p2)

   # for i in range(0, 100 + 1, 2):
    #    t = i / 100
     #   x = (1 - t) * p1[0] + t * p2[0]
      #  y = (1 - t) * p1[1] + t * p2[1]
       # draw_point((x, y))

    #draw_point(p2)


open_canvas(KPU_WIDTH, KPU_HEIGHT)
kpu_ground = load_image('KPU_GROUND.png')
arrow = load_image('hand_arrow.png')
character = load_image('animation_sheet.png')

running = True
x, y = KPU_WIDTH // 2, KPU_HEIGHT // 2
cx, cy = KPU_WIDTH // 2, KPU_HEIGHT // 2
frame = 0
hide_cursor()

while running:
    clear_canvas()
    kpu_ground.draw(KPU_WIDTH // 2, KPU_HEIGHT // 2)
    arrow.draw(x, y)
    character.clip_draw(frame * 100, 100 * 1, 100, 100, cx,KPU_HEIGHT - 1 - cy)
    update_canvas()
    frame = (frame + 1) % 8

    handle_events()

close_canvas()