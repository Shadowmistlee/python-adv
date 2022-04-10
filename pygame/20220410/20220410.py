from turtle import back
import pygame
import sys
import math
import random
from pygame.display import get_window_size
import os
import time

os.chdir(sys.path[0])
from pygame.locals import *

os.chdir(sys.path[0])
pygame.init()


def check_click(pos, x_min, y_min, x_max, y_max):
    x_match = pos[0] > x_min and pos[0] < x_max
    y_match = pos[1] > y_min and pos[1] < y_max
    if x_match and y_match:
        return True
    else:
        return False


bg_img = "C:/Users/Xavier/Desktop/python-adv/pygame/20220410/Gophers_BG_800x600.png"
pygame.mouse.set_visible(False)
bg = pygame.image.load(bg_img)
bg_x = bg.get_width()
bg_y = bg.get_height()
BLUE = (0, 0, 255)
BLACK = (0, 0, 0)
screen = pygame.display.set_mode([bg_x, bg_y])
gophers = pygame.image.load(
    "C:/Users/Xavier/Desktop/python-adv/pygame/20220410/Gophers150.png")
pygame.display.set_caption("Gameeeeeeeee")
typeface = pygame.font.get_default_font()
sur = pygame.Surface([bg_x, bg_y])  #繪製背景容器
font = pygame.font.Font(typeface, 24)
pos6 = [[195, 305], [400, 305], [610, 305], [195, 450], [400, 450], [610, 450]]
num = 0
title = font.render(str(num), True, (255, 255, 255))
tick = 0
max_tick = 20
mpos = (0, 0)
pos = pos6[0]
times = 0
times_max = 20
clock = pygame.time.Clock()
end_font = pygame.font.Font(typeface, 36)
end_sur = end_font.render(str(times), True, (255, 0, 0))
score = 0
ham1 = pygame.image.load("Hammer1.png")
ham2 = pygame.image.load("Hammer2.png")
while True:
    clock.tick(30)
    hammer = ham2
    mouse_pos = pygame.mouse.get_pos()
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
        if event.type == pygame.MOUSEBUTTONDOWN:
            hammer = ham1
            if check_click(mouse_pos, pos[0] - 50, pos[1] - 50, pos[0] + 50,
                           pos[1] + 50):
                if times < times_max:
                    tick = max_tick + 1
                    score = score + 1
        if event.type == pygame.MOUSEMOTION:
            mpos = pygame.mouse.get_pos()
    if times > times_max:
        sur.fill((0, 0, 0))
        pygame.mouse.set_visible(True)
        end_sur = title.render("Your Score is:{}/{}".format(score, times_max),
                               False)
        screen.blit(sur, (0, 0))
        screen.blit(end_sur, (100, 100))
        pygame.display.update()

    sur.blit(bg, (0, 0))
    if tick > max_tick:
        new_pos = random.randint(0, 5)
        pos = pos6[new_pos]
        tick = 0

        title = font.render(str(num), True, (255, 255, 255))
    else:
        tick += 1
        title = font.render(str(num), True, (255, 255, 255))

    sur.blit(
        gophers,
        (pos[0] - gophers.get_width() / 2, pos[1] - gophers.get_height() / 2))

    # pygame.draw.circle(sur, BLUE, pos, 50)
    sur.blit(
        hammer,
        (mpos[0] - hammer.get_width() / 2, mpos[1] - hammer.get_height() / 2))
    screen.blit(sur, (0, 0))
    screen.blit(title, (10, 10))
    if hammer == ham1:
        time.sleep(0.1)
    pygame.display.flip()