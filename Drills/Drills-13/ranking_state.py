import random
import json
import pickle
import os

from pico2d import *
import game_framework
import game_world

import world_build_state

name = "Ranking_state"

font = load_font("ENCR10B.TTF", 20)

time_ls = []

def enter():
    global file
    file = json.load('rankTime.json')

def exit():
    game_world.clear()

def pause():
    pass


def resume():
    pass


def handle_events():
    events = get_events()
    for event in events:
        if event.type == SDL_QUIT:
            game_framework.quit()
        elif event.type == SDL_KEYDOWN and event.key == SDLK_ESCAPE:
            game_framework.change_state(world_build_state)



def update():
    global file
    for data in file:
        time_ls.append(data['time'])
    time_ls.sort()



def draw():
    clear_canvas()
    num = 0
    while num < 10:
        font.draw(60, (10 - num) * 10, '(#%d: %3.2f)' %num%time_ls[num], (0, 0, 0))
    update_canvas()






