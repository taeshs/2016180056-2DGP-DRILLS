from pico2d import *


class Platform:
    def __init__(self):
        self.image = load_image('brick180x40.png')
        self.x, self.y = 800, 200
        self.dir = 1

    def update(self):
        if self.dir == 1:
            self.x += 1
            if self.x > 1200 - 90:
                self.dir = 0
        if self.dir == 0:
            self.x -= 1
            if self.x < 0 + 90:
                self.dir = 1

    def draw(self):
        self.image.draw(self.x, self.y)
        draw_rectangle(*self.get_bb())

    def get_bb(self):
        return self.x - 90, self.y - 20, self.x + 90, self.y + 20
