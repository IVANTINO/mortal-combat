import pygame
import os
import sys
import random

pygame.init()
current_path = os.path.dirname(__file__)
os.chdir(current_path)
WIDTH = 1200
HEIGHT = 600
FPS = 60
sc = pygame.display.set_mode((WIDTH, HEIGHT))
clock = pygame.time.Clock()
font = pygame.font.SysFont('arol', 40)
from load import *


def restart():
    global fon, player1
    fon = FON()
    player1 = Player_1


def game_lvl():
    sc.fill("grey")
    fon.update()
    player1.update()
    pygame.display.update()


class FON:
    def __init__(self):
        self.timer = 0
        self.frame = 0
        self.image = fon_image

    def update(self):
        self.timer += 2
        sc.blit(self.image[self.frame], (0, 0))
        if self.timer / FPS > 0.1:
            if self.frame == len(self.image) - 1:
                self.frame = 0
            else:
                self.frame += 1
            self.timer = 0


class Player_1(pygame.sprite.Sprite):
    def __init__(self, image_list):
        pygame.sprite.Sprite.__init__(self)
        self.image_list = image_list
        self.image = self.image_list['idle'][0]
        self.current_list_image = self.image_list['idle']
        self.rect = self.image.get_rect()
        self.anime_idle = True
        self.anime_run = False
        self.anime_atk = False
        self.frame = 0
        self.timer_anime = 0
        self.dir = "right"
        self.hp = 100
        self.jump_step = -15
        self.jump = False
        self.mask = pygame.mask.from_surface(self.image)
        self.mask_outline = self.mask.outline()
        self.mask.list = []
        self.rect.center = (200, 380)
        self.hp_bar = "blue"
        self.key = pygame.key.get_pressed()

    def move(self):
        if self.key[pygame.K_d]:
            self.rect.x += 2
            self.anime_idle = False
            if not self.anime_atk:
                self.anime_run = True
        elif self.key[pygame.K_a]:
            self.rect.x -= 2
            self.anime.idle = False
            if not self.anime_atk:
                self.anime_run = True

        else:
            if not self.anime_atk:
                self.anime_idle = True
            self.anime_run = False

    def jumps(self):
        if self.key[pygame.K_SPACE]:
            self.jump=True
        if self.jump:
            if self.jump_step<=20:
                self.rect.y+=self.jump_step
                self.jump_step+=1
            else:
                self.jump=False
                self.jump_step=-20

    def attack(self):
        if self.key[pygame.K_e] and not self.anime_atk:
            self.frame=0
            self.anime_atk=True
            self.anime_idle=False
            self.anime_run=False
            self.flag_damage=True

    def animation(self):
        self.timer_anime+=2
        if self.timer_anime/FPS>0.1:
            if self.frame==len(self.current_list_image)-1:
                self.frame=0
                if self.anime_atk:
                    self.current_list_image=player1_idle_image
                    self.anime_atk=False
                    self.anime_idle=True
            else:
                self.frame+=1
            self.timer_anime=0
        if self.anime_idle:
            self.current_list_image=self.image_lists['idle']
        elif self.anime_run:
            self.current_list_image=self.image_lists['run']
        elif self.anime_atk:
            self.current_list_image=self.image_lists['atk']
        try:
            if self.dir =="right":
                self.image= self.current_list_image[self.frame]
            else:
                self.image=pygame.transform.flip(self.current_list_image[self.frame],True,False)
        except:
            self.frame=0


    def update(self):
        if self.rect.center[0] - player_2.rect.center[0] < 0:
            self.dir = "right"
        else:
            self.dir = "left"
        self.key = pygame.key.get_pressed()
        self.move()
        self.animation()
        self.attack()
        self.jumps()
        self.draw_hp_bar()


restart()

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
    game_lvl()
    clock.tick(FPS)
