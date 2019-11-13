import random
from pico2d import *
import game_world
import game_framework
from platform import Platform

class Ball:
    image = None

    def __init__(self):
        if Ball.image == None:
            Ball.image = load_image('ball21x21.png')
        self.x, self.y, self.fall_speed = random.randint(0, 1600-1), 60, 0
        self.isonplat = False

    def get_bb(self):
        return self.x - 10, self.y - 10, self.x + 10, self.y + 10

    def draw(self):
        self.image.draw(self.x, self.y)
        draw_rectangle(*self.get_bb())

    def update(self):
        if self.isonplat:
            self.y ==
        else:
            self.y -= self.fall_speed * game_framework.frame_time
        self.y = clamp(50 + 20, self.y, 600)

    def stop(self):
        self.fall_speed = 0



class BigBall(Ball):
    MIN_FALL_SPEED = 50
    MAX_FALL_SPEED = 200
    image = None

    def __init__(self):
        if BigBall.image == None:
            BigBall.image = load_image('ball41x41.png')
        self.x, self.y = random.randint(0, 1600-1), 500
        self.fall_speed = random.randint(BigBall.MIN_FALL_SPEED,
                                         BigBall.MAX_FALL_SPEED)

    def get_bb(self):
        return self.x - 20, self.y - 20, self.x + 20, self.y + 20
