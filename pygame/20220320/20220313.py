from turtle import back
import pygame
import sys
import math
import random
from pygame.display import get_window_size

pygame.init()


def check_click(pos, x_min, y_min, x_max, y_max):
    x_match = pos[0] > x_min and pos[0] < x_max
    y_match = pos[1] > y_min and pos[1] < y_max
    if x_match and y_match:
        return True
    else:
        return False


width = 640

height = 320

screen = pygame.display.set_mode((width, height))
pygame.display.set_caption("Gameeeeeeeee")
background = pygame.image.load(
    "C:/Users/Xavier/Desktop/python-adv/pygame/20220320/snow.jpg")
bg_x = background.get_width()
bg_y = background.get_height()
mp3_path = 'pygame/20220320/music.mp3'
pygame.mixer.music.load(mp3_path)
pygame.mixer.music.play()
pygame.mixer.music.fadeout(600000)
act = False
typeface = pygame.font.get_default_font()
font = pygame.font.Font(typeface, 24)
title = font.render('start', True, (0, 0, 0))
tit_w = title.get_width()
tit_h = title.get_height()
title2 = font.render('slow', True, (0, 0, 0))
tit2_w = title2.get_width()
tit2_h = title2.get_height()
snow_list = []
for i in range(100):
    x_site = random.randrange(0, bg_x)
    y_site = random.randrange(-10, -1)
    x_shift = random.randint(-1, 1)
    radius = random.randint(4, 6)
    snow_list.append([x_site, y_site, x_shift, radius])
snow_list[1][0]
clock = pygame.time.Clock()
act = False
cnt = 0
speed = False
while True:
    if cnt <= 10:
        cnt += 1
    else:
        cnt = 0
        x_shift = random.randint(-5, 5)

    if speed == True:
        clock.tick(20)
        title2 = font.render('slow', True, (
            0,
            0,
            0,
        ))
    else:
        clock.tick(70)
        title2 = font.render('fast', True, (
            0,
            0,
            0,
        ))
    screen.blit(background, (0, 0))
    mouse_pos = pygame.mouse.get_pos()
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
        if event.type == pygame.MOUSEBUTTONDOWN:
            if check_click(mouse_pos, 0, 0, tit_w, tit_h):
                act = not (act)
            if check_click(mouse_pos, 100, 0, int(tit2_w) + 100, int(tit2_h)):
                speed = not (speed)

    if act == True:
        title = font.render('Start', True, (
            0,
            0,
            0,
        ))
        pygame.mixer.music.unpause()
    else:
        title = font.render('Stop', True, (
            0,
            0,
            0,
        ))

        #pygame.draw.circle(screen, (255, 255, 255), (x_site, y_site), radius)
        for snow in snow_list:
            pygame.draw.circle(screen, (255, 255, 255), (snow[0], snow[1]),
                               snow[3])
            snow[0] += snow[2]
            snow[1] += snow[3]
            if snow[1] > bg_y or snow[0] > bg_x:
                snow[1] = random.randrange(-1000, -1)
                snow[0] = random.randrange(0, bg_x)
    screen.blit(title, (0, 0))
    screen.blit(title2, (100, 0))

    pygame.display.update()
