import game_framework
from pico2d import *
import main_state


name = "PauseState"
image = None
dtime = 0


def enter():
    global image
    image = load_image('pause.png')


def exit():
    global image
    del(image)


def handle_events():
    events = get_events()
    for event in events:
        if event.type == SDL_QUIT:
            game_framework.quit()
        else:
            if event.type == SDL_KEYDOWN and event.key == SDLK_p:
                game_framework.pop_state()
                main_state.draw()


def draw():
    global dtime
    clear_canvas()
    if(dtime < 0.5):
        image.draw(400, 300)
    main_state.draw()
    update_canvas()
    delay(0.01)
    dtime = (dtime + 0.01) % 1

def update():
    pass


def pause():
    pass


def resume():
    pass
