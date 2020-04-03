  
# Sprite classes for platform game
import pygame as pg
from pygame.sprite import Sprite
from settings import *
vec = pg.math.Vector2

class Player(Sprite):
    def __init__(self, game):
        Sprite.__init__(self)
        self.game = game
        self.image = pg.Surface((30, 45))
        self.image.fill(WHITE)
        self.rect = self.image.get_rect()
        self.rect.center = (WIDTH / 2, HEIGHT / 2)
        self.pos = vec(WIDTH / 2, HEIGHT / 2)
        self.vel = vec(0, 0)
        self.acc = vec(0, 0)
    def myMethod(self):
        pass
    def jump(self):
        self.rect.x += 1
        hits = pg.sprite.spritecollide(self, self.game.platforms, False)
        self.rect.x -= -1
        if hits:
            self.vel.y = -40
    # def death(self):
    #     deathJump = pg.sprite.spritecollide(self, self.game.death, False)
    def update(self):
        self.acc = vec(0, 0.5)
        keys = pg.key.get_pressed()
        if keys[pg.K_LEFT]:
            self.acc.x = -PLAYER_ACC
        if keys[pg.K_RIGHT]:
            self.acc.x = PLAYER_ACC
        # if keys[pg.K_UP]:
        #     self.acc.y = -PLAYER_ACC
        if keys[pg.K_DOWN]:
            self.acc.y = PLAYER_ACC
        if keys[pg.K_SPACE]:
            self.jump()

        # apply friction
        self.acc += self.vel * PLAYER_FRICTION
        # equations of motion
        self.vel += self.acc
        self.pos += self.vel + 0.5 * self.acc
        # wrap around the sides of the screen
        if self.pos.x > WIDTH:
            self.pos.x = 0
        if self.pos.x < 0:
            self.pos.x = WIDTH
        if self.pos.y < 0:
            self.pos.y = HEIGHT
        if self.pos.y > HEIGHT:
            self.pos.y = 0

        self.rect.center = self.pos

class Platform(Sprite):
    def __init__(self, color, x, y, w, h, velx, vely):
        Sprite.__init__(self)
        self.image = pg.Surface((w,h))
        self.image.fill(color)
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.vx = velx
        self.vy = vely
    def update(self):
        self.rect.x += self.vx
        self.rect.y += self.vy
        if self.rect.x >= WIDTH-10:
            self.vx = -self.vx
        if self.rect.x <= 10:
            self.vx = -self.vx
        if self.rect.y <= 10:
            self.vy = -self.vy
        if self.rect.y > HEIGHT-10:
            self.vy = -self.vy

class Goal(Sprite):
    def __init__(self, game):
        Sprite.__init__(self)
        self.image = pg.Surface((75,20))
        self.image.fill(YELLOW)
        self.rect = self.image.get_rect()
        self.rect.y = 600
        self.rect.x = WIDTH/2

# class Death(Sprite):
#     def __init__(self, x, y, w, h, velx, vely):
#         Sprite.__init__(self)
#         self.image = pg.Surface((w,h))
#         self.image.fill(RED)
#         self.rect = self.image.get_rect()
#         self.rect.x = x
#         self.rect.y = y
#         self.vx = velx
#         self.vy = vely
#     def update(self):
#         self.rect.x += self.vx
#         self.rect.y += self.vy
#         if self.rect.x >= WIDTH-10:
#             self.vx = -self.vx
#         if self.rect.x <= 10:
#             self.vx = -self.vx
#         if self.rect.y <= 10:
#             self.vy = -self.vy
#         if self.rect.y > HEIGHT-10:
#             self.vy = -self.vy
        

