import pygame
import sys
import math

from pygame.display import get_window_size

pygame.init()

width = 640

height = 320

screen = pygame.display.set_mode((width, height))
pygame.display.set_caption("Gameeeeeeeee")
background = pygame.Surface(screen.get_size())
background.fill((255, 255, 255))
act = False
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
        if event.type == pygame.MOUSEBUTTONDOWN:
            act = not (act)
    if act:
        pygame.draw.circle(background, (0, 0, 255), (200, 100), 30, 0)
        pygame.draw.circle(background, (0, 0, 0), (200, 100), 10, 0)
        pygame.draw.circle(background, (0, 0, 255), (100, 100), 30, 0)
        pygame.draw.circle(background, (0, 0, 0), (100, 100), 10, 0)
        pygame.draw.rect(background, (0, 255, 0), [0, 0, 255, 255], 5)
        # pygame.draw.ellipse(background, (255, 0, 0), [130, 160, 60, 35], 5)
        # pygame.draw.polygon(background, (100, 200, 45),
        #                     [[100, 100], [0, 200], [200, 200]], 0)
        pygame.draw.arc(background, (255, 10, 0), [100, 200, 100, 50],
                        math.radians(0), math.radians(360), 2)
    else:
        background.fill((255, 255, 255))
    screen.blit(background, (0, 0))
    pygame.display.update()
