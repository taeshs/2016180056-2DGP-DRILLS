import game_framework
from pico2d import *

import game_world

# bird Run Speed FLY
PIXEL_PER_METER = (10.0 / 0.3)
FLY_SPEED_KMPH = 50.0
FLY_SPEED_MPM = (FLY_SPEED_KMPH * 1000.0 / 60.0)
FLY_SPEED_MPS = (FLY_SPEED_MPM / 60.0)
FLY_SPEED_PPS = (FLY_SPEED_MPS * PIXEL_PER_METER)

# bird Action Speed
TIME_PER_ACTION = 0.25
ACTION_PER_TIME = 1.0 / TIME_PER_ACTION
FRAMES_PER_ACTION = 14



# bird States

class IdleState:

    @staticmethod
    def enter(bird, event):
        pass

    @staticmethod
    def exit(bird, event):
        pass

    @staticmethod
    def do(bird):
        if bird.dir == 1:
            bird.velocity = FLY_SPEED_PPS
            bird.x += bird.velocity * game_framework.frame_time
            if bird.x > 1600 - 75:
                bird.dir = 0
        if bird.dir == 0:
            bird.velocity = -1 * FLY_SPEED_PPS
            bird.x += bird.velocity * game_framework.frame_time
            if bird.x < 0 + 25:
                bird.dir = 1
        if 0 < bird.frame < 6:
            bird.imageY = 168 * 2
        elif bird.frame < 11:
            bird.imageY = 168
        else:
            bird.imageY = 0

        bird.frame = (bird.frame + FRAMES_PER_ACTION * ACTION_PER_TIME * game_framework.frame_time) % 14


    @staticmethod
    def draw(bird):
            bird.image.clip_draw((int(bird.frame) % 5) * 183 , bird.imageY, 183, 168, bird.x, bird.y, 75, 75)

# 새 크기 1.65 미터



class Bird:

    def __init__(self):
        self.x, self.y = 1600 // 2, 300
        self.image = load_image('bird_animation.png')
        self.dir = 1
        self.imageY = 168 * 2
        self.velocity = 0
        self.frame = 0
        self.event_que = []
        self.cur_state = IdleState
        self.cur_state.enter(self, None)


    def update(self):
        self.cur_state.do(self)


    def draw(self):
        self.cur_state.draw(self)
