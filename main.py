###This file was altered/created by: Akshaj Dwivedula

# KidsCanCode - Game Development with Pygame video series
# Jumpy! (a platform game) - Part 2
# Video link: https://www.youtube.com/watch?v=8LRI0RLKyt0
# Player movement

# Copyright 2019 KidsCanCode LLC -/- All rights reserved.

import pygame as pg
from pygame.sprite import Group
import random as rand
from settings import *
from sprites import *
import math

class Game:
    def __init__(self):
        # initialize game window, etc
        pg.init()
        pg.mixer.init()
        self.screen = pg.display.set_mode((WIDTH, HEIGHT))
        pg.display.set_caption(TITLE)
        self.clock = pg.time.Clock()
        self.running = True

    def new(self):
        # start a new game
        self.all_sprites = Group()
        self.deaths = pg.sprite.Group()
        self.goals = pg.sprite.Group()
        goal = Goal(self)
        self.all_sprites.add(goal)
        self.goals.add(goal)
        self.platforms = pg.sprite.Group()
        self.player = Player(self)
        self.all_sprites.add(self.player)
        ground = Platform(GREEN,0, HEIGHT-40, WIDTH, 40, 0, 0)
        self.all_sprites.add(ground)
        self.platforms.add(ground)
        # for x in range(0,5):
        #     x = Platform(BLUE, rand.randint(100,400),rand.randint(100,500), rand.randint(50, WIDTH-100), rand.randint(10, 40), rand.randint(0,5), 0 )
        #     self.all_sprites.add(x)
        #     self.platforms.add(x)
        
        self.run()

    def run(self):
        # Game Loop
        self.playing = True
        while self.playing:
            self.clock.tick(FPS)
            self.events()
            self.update()
            self.draw()

    def update(self):
        # Game Loop - Update
        self.all_sprites.update()
        hits = pg.sprite.spritecollide(self.player, self.platforms, False)
        # if hits and self.player.pos.y == hits[0].rect.bottom:
        #     self.player.vel.y = -self.player.vel.y
        if hits:
            #This code was copied from Mr. Cozort's test file
            if self.player.rect.top > hits[0].rect.top:
                self.player.vel.y = 15
                self.player.rect.top = hits[0].rect.bottom + 5
            else:
                self.player.vel.y = 0
                self.player.pos.y = hits[0].rect.top-20
        # if hits and self.player.pos.y == hits[0].rect.bottom:
        #     self.player.vel.y = -self.player.vel.y
        if hits:
            #This code was copied from Mr. Cozort's test file
            if self.player.rect.top > hits[0].rect.top:
                self.player.vel.y = 15
                self.player.rect.top = hits[0].rect.bottom + 5
            else:
                self.player.vel.y = 0
                self.player.pos.y = hits[0].rect.top-20
        win = pg.sprite.spritecollide(self.player, self.goals, False)
        if win:
            if self.player.rect.top > hits[0].rect.top:
                self.player.vel.y = 15
                self.player.rect.top = hits[0].rect.bottom + 5
            else:
                self.player.vel.y = 0
                print("You win the game")
                self.playing = False

            

    def events(self):
        # Game Loop - events
        for event in pg.event.get():
            # check for closing window
            if event.type == pg.QUIT:
                if self.playing:
                    self.playing = False
                self.running = False

    def draw(self):
        # Game Loop - draw
        self.screen.fill(BLACK)
        self.all_sprites.draw(self.screen)
        # *after* drawing everything, flip the display
        pg.display.flip()

    def show_start_screen(self):
        # game splash/start screen
        pass

    def show_go_screen(self):
        # game over/continue
        pass

g = Game()
g.show_start_screen()
while g.running:
    g.new()
    g.show_go_screen()

pg.quit()