  
# Sprite classes for platform game
import pygame as pg
from pygame.sprite import Sprite
from settings import *
vec = pg.math.Vector2
##this player sprite is the same as the sprite from Chris Bradford's code, with slight modification for size and color
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
        hits = pg.sprite.spritecollide(self, self.game.boards, False)
        self.rect.x -= -1
        #this setting is allowing a jump when on a board/platform. If hits, then they can jump upward
        if hits:
            self.vel.y = -40
    def update(self):
        self.acc = vec(0, 0.5)
        keys = pg.key.get_pressed()
        if keys[pg.K_LEFT]:
            self.acc.x = -PLAYER_ACC
        if keys[pg.K_RIGHT]:
            self.acc.x = PLAYER_ACC
        #got rid of the up button because it allows the player to fly
        # if keys[pg.K_UP]:
        #     self.acc.y = -PLAYER_ACC
        if keys[pg.K_DOWN]:
            self.acc.y = PLAYER_ACC
        #runs the method jump
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

'''Moving platforms took the existing platform class and just added velocity components by adding in velx and vely to represent self.vx and self.vy
    The addition of an additional set of if statements is there to make sure the platforms look like they are moving from left to right across the play area.
    Platforms are then ascribed different roles in the game based on their color - ORANGE is the goal, RED is an enemy, and BLUE is a safety zone.
    All three are part of the moving platform class but are added to different sprite groups that interact with the user in different ways - essentially creating a pseudo-subclass'''
class Platform(Sprite):
    #platform sprites can be customized to a large extent - critical difference is the color and the speed
    def __init__(self, color, x, y, w, h, velx, vely):
        Sprite.__init__(self)
        self.image = pg.Surface((w,h))
        self.image.fill(color)
        self.rect = self.image.get_rect()
        #sets x and y coordinates equal to the x and y variables in the initialization
        self.rect.x = x
        self.rect.y = y
        #sets velocities equal to the velx and vely variables in the initialization
        self.vx = velx
        self.vy = vely
    def update(self):
        #basic velocity
        self.rect.x += self.vx
        self.rect.y += self.vy
        #when it reaches the edges, velocity flips so it can move in the opposite direction
        if self.rect.x >= WIDTH-10:
            self.vx = -self.vx
        if self.rect.x <= 10:
            self.vx = -self.vx
        if self.rect.y <= 10:
            self.vy = -self.vy
        if self.rect.y > HEIGHT-10:
            self.vy = -self.vy

#was another class here - the Goal Sprite but that is actually unnecessary so the Goal class was removed


        

