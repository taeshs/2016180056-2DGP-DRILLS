import random
from pico2d import *
import game_world
import game_framework
import main_state


class Ball:
    image = None

    def __init__(self):
        if Ball.image == None:
            Ball.image = load_image('ball21x21.png')
        self.x, self.y = random.randint(0, 1800), random.randint(0, 1050)
        self.isonplat = False
        self.boy = main_state.get_boy()

    def get_bb(self):
        return self.cx - 10, self.cy - 10, self.cx + 10, self.cy + 10

    def set_background(self, bg):
        self.bg = bg

    def draw(self):
        self.image.draw(self.cx, self.cy)
        draw_rectangle(*self.get_bb())

    def update(self):
        self.cx, self.cy = self.x - (self.bg.window_left), self.y - (self.bg.window_bottom)
