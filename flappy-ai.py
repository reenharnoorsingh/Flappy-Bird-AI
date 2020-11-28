# importing modules
import pygame
import neat
import time
import os
import random

# set screen dimensions
WINDOW_HEIGHT = 800
WINDOW_WIDTH = 600

# loading images
BIRD_IMGS = [pygame.transform.scale2x(pygame.image.load(os.path.join("imgs", "bird1.png",))), pygame.transform.scale2x(
    pygame.image.load(os.path.join("imgs", "bird2.png",))), pygame.transform.scale2x(pygame.image.load(os.path.join("imgs", "bird3.png",)))]
PIPE_IMG = [pygame.transform.scale2x(
    pygame.image.load(os.path.join("imgs", "pipe.png",)))]
BG_IMG = [pygame.transform.scale2x(
    pygame.image.load(os.path.join("imgs", "bg.png",)))]
BASE_IMG = [pygame.transform.scale2x(
    pygame.image.load(os.path.join("imgs", "base.png",)))]

# BIRD CLASS


class Bird:
    IMGS = BIRD_IMGS
    # constants
    MAX_ROTATION = 25  # the tilting of bird
    ROT_VEL = 20  # rotation on each frame
    ANIMATION_TIME = 5  # showing each animation

    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.tilt = 0
        self.tick_count = 0
        self.vel = 0
        self.height = self.y
        self.img_count = 0
        self.img = self.IMGS[0]

    def jump(self):
        self.vel = -10.5
        self.tick_count = 0
        self.height = self.y

    def move(self):
        self.tick_count += 1

        d = self.vel*self.tick_count + 1.5*self.tick_count**2

        if d >= 16:  # terminal velocity
            d = 16

        if d < 0:
            d -= 2

        self.y = self.y+d

        if
