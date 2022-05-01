#===載入套件開始
import pygame
import sys
import os

os.chdir(sys.path[0])
from pygame.locals import *
#***載入套件結束***

#===初始化設定開始===
LIMIT_LOW = 140
LIMIT_HIGH = 140
pygame.init()
timer = 0
clock = pygame.time.Clock()
#***初始化設定結束***

#===載入圖片開始===
img = pygame.image.load(
    "C:/Users/Xavier/Desktop/python-adv/pygame/20220417/bg.png")
img_dinosaur = [
    pygame.image.load(
        "C:/Users/Xavier/Desktop/python-adv/pygame/20220417/小恐龍1.png"),
    pygame.image.load(
        "C:/Users/Xavier/Desktop/python-adv/pygame/20220417/小恐龍2.png")
]
img_cacti = pygame.image.load(
    "C:/Users/Xavier/Desktop/python-adv/pygame/20220417/cacti.png")
img_gg = pygame.image.load(
    "C:/Users/Xavier/Desktop/python-adv/pygame/20220424/gameover.png")

# 載入圖片結束

#===遊戲視窗設定開始===
bg_x = img.get_width()
bg_y = img.get_height()
bg_size = (bg_x, bg_y)
roll_x = 0

pygame.display.set_caption("Dinosaur")
screen = pygame.display.set_mode(bg_size)
#***遊戲視窗設定結束***

#===分數設定開始===
score = 0
typeface = pygame.font.get_default_font()
score_font = pygame.font.Font(typeface, 36)


def get_score(win):
    global score
    score_sur = score_font.render(str(score), True, (255, 0, 0))
    win.blit(score_sur, [10, 10])


#***分數設定結束***

#===恐龍設定開始===
ds_x = 50
ds_y = LIMIT_LOW
jumpValue = 0
jumpState = False


def move_dinosaur(win, timer):
    global ds_x, ds_y, jumpState, jumpValue
    if jumpState:
        if ds_y >= LIMIT_LOW:
            jumpValue = -10
        if ds_y <= 0:
            jumpValue = 10
        ds_y += jumpValue
        if ds_y >= LIMIT_LOW:
            jumpState = False
    win.blit(img_dinosaur[timer % 20 // 10], [ds_x, ds_y])


#***恐龍設定結束***

#===仙人掌設定開始===
cacti_w = img_cacti.get_width()
cacti_h = img_cacti.get_height()
cacti_x = bg_x - 100
cacti_y = LIMIT_LOW
cacti_shift = 10
cacti_dist = int((cacti_w + cacti_h) / 2)


def move_cacti(win):
    global cacti_x, cacti_y, cacti_shift
    global score
    cacti_x -= cacti_shift
    if (cacti_x < 0):
        score += 1
        cacti_x = bg_x - 100
        cacti_shift = 10

    win.blit(img_cacti, [cacti_x, cacti_y])
    # cacti_x = (cacti_x - cacti_shift) % bg_x


#***仙人掌設定結束***


#***碰撞設定結束***
def is_hit(x1, y1, x2, y2, r):
    if ((x1 - x2) * (x1 - x2) + (y1 - y2) * (y1 - y2)) < (r * r):
        return True
    else:
        return False


#***碰撞設定結束***

#===GameOver設定開始===
gg = False
gg_w = img_gg.get_width()
gg_h = img_gg.get_height()


def game_over(win):
    win.blit(img_gg, ((bg_x - gg_w) / 2, (bg_y - gg_h) / 2))


#***GameOver設定結束***

#===主程式開始===
while True:
    #===計時與速度===
    clock.tick(20)
    timer += 1
    #===偵測鍵盤事件開始===
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
        if event.type == KEYDOWN:
            if event.key == K_SPACE and ds_y <= LIMIT_LOW:
                jumpState = True
            elif event.key == K_RETURN and gg == True:
                gg = False
                cacti_x = bg_x - 100
                ds_x = 50
                ds_y = LIMIT_LOW
                score = 0
                jumpState = False

    if (gg == True):
        #===遊戲結束===
        game_over(screen)
    else:

        #===遊戲進行===
        roll_x = (roll_x - 10) % bg_x
        # print(roll_x)
        screen.blit(img, [roll_x - bg_x, 0])
        screen.blit(img, [roll_x, 0])

        #===更新角色狀態===
        move_dinosaur(screen, timer)
        move_cacti(screen)
        get_score(screen)
        if (is_hit(ds_x, ds_y, cacti_x, cacti_y, cacti_dist)):
            gg = True
    pygame.display.update()
#===主程式結束===