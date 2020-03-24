##This file was created by: Akshaj Dwivedula

import pygame
from pygame.sprite import Sprite
from settings import *


class Player(Sprite):
    # sprite for player
    # properties of the class
    def __init__(self):
        Sprite.__init__(self)
        self.image = pygame.Surface((50,50))
        self.image.fill(BLACK)
        '''sets image path to correct location joining image folder to file name then converting to a more efficient format'''
        # self.image = pygame.image.load(os.path.join(img_folder, "Tie.png")).convert()
        '''sets transparent color key to black'''
        # self.image.set_colorkey(BLACK)
        self.rect = self.image.get_rect()
        self.rect.center = (WIDTH / 2, HEIGHT / 2)
        # self.screen_rect = screen.get_rect()
        self.vx = 0
        self.vy = 0
        self.cofric = 0.5
        self.canjump = False
    # stuff it can do....
    def friction(self):
        self.cofric = .25
        if self.vx > 0.5:
            self.vx -= self.cofric
        elif self.vx < -0.5:
            self.vx += self.cofric
        else:
            self.vx = 0
        if self.vy < -0.5:
            self.vy += self.cofric
        elif self.vy > 0.5:
            self.vy -= self.cofric
        else:
            self.vy = 0
    def jump(self):
        if self.canjump == True:
            self.canjump = False
            self.vy -= 50
    def gravity(self, value):
        self.vy += value
    def update(self):
        self.friction()
        if self.rect.bottom < HEIGHT:
            self.gravity(9.8)
        if self.rect.right > WIDTH:
            self.rect.right = WIDTH
        if self.rect.left < 0:
            self.rect.left = 0
        if self.rect.bottom > HEIGHT:
            self.rect.bottom = HEIGHT
            self.vy = 0
            self.canjump = True
        if self.rect.top < 0:
            self.rect.top = 0
            self.vy = 0
        self.rect.x += self.vx
        self.rect.y += self.vy
        # if self.rect.right > 790:
        #     self.vx = -2
        # if self.rect.right < 10:
        #     self.vx = 2
        # if self.rect.top > 590:
        #     self.vy = -2
        # if self.rect.top < 10:
        #     self.vy = 2
        keystate = pygame.key.get_pressed()
        if keystate[pygame.K_w]:
            self.vy -= 1
        if keystate[pygame.K_a]:
            self.vx -= 1
        if keystate[pygame.K_s]:
            self.vy += 1
        if keystate[pygame.K_d]:
            self.vx += 1
        if keystate[pygame.K_x]:
            self.vx = 0 
            self.vy = 0
        if keystate[pygame.K_SPACE]:
            self.jump()
        # if keystate[pygame.K_SPACE]:
        #     self.shoot()
        # if self.rect.right > WIDTH:
        #     self.rect.right = WIDTH
        # if self.rect.left < 0:
        #     self.rect.left = 0
        # if self.rect.bottom > HEIGHT:
        #     self.rect.bottom = HEIGHT
        # if self.rect.top < 0:
        #     self.rect.top = 0
    
    # def hitWall():


class Enemy(Sprite):
    # sprite for enemy
    # properties of the class
    def __init__(self):
        Sprite.__init__(self)
        #makes enemy different color and a little smaller than the player
        self.image = pygame.Surface((35,35))
        self.image.fill(WHITE)
        '''sets image path to correct location joining image folder to file name then converting to a more efficient format'''
        # self.image = pygame.image.load(os.path.join(img_folder, "Tie.png")).convert()
        '''sets transparent color key to black'''
        # self.image.set_colorkey(BLACK)
        self.rect = self.image.get_rect()
        self.rect.center = (WIDTH / 2, HEIGHT / 2)
        # self.screen_rect = screen.get_rect()
        self.vx = -3
        self.vy = -2
        self.cofric = 0.5
    # stuff it can do....
    def update(self):
        self.rect.x += self.vx
        self.rect.y += self.vy
        if self.rect.right > 800:
            self.vx = -3
        if self.rect.left < 0:
            self.vx = 3
        if self.rect.top > 600:
            self.vy = -2
        if self.rect.bottom < 0:
            self.vy = 2
        # if keystate[pygame.K_SPACE]:
        #     self.shoot()
        # if self.rect.right > WIDTH:
        #     self.rect.right = WIDTH
        # if self.rect.left < 0:
        #     self.rect.left = 0
        # if self.rect.bottom > HEIGHT:
        #     self.rect.bottom = HEIGHT
        # if self.rect.top < 0:
        #     self.rect.top = 0
    # def hitWall():
# init pygame and create window