###This file was altered/created by: Akshaj Dwivedula

# KidsCanCode - Game Development with Pygame video series
# Jumpy! (a platform game) - Part 2
# Video link: https://www.youtube.com/watch?v=8LRI0RLKyt0
# Player movement

# Copyright 2019 KidsCanCode LLC -/- All rights reserved.
#Citations: Some code was taken/modified from Mr. Cozort's test file


#importing libraries from pythong - as feature provides shorthand for coding
import pygame as pg
from pygame.sprite import Group
import random as rand
#modularity - importng both the settings and the sprites file and the properties from said files
from settings import *
from sprites import *
import math

class Game:
    #by setting class Game, all sprites settings that have self.game now just become self
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
        #sets up all the various groups necessary for the game including the allsprites and the various single sprite groups
        self.all_sprites = Group()
        #boards is the general group for all non-player sprites
        self.boards = pg.sprite.Group()
        #deaths is the group for the "lava" platforms
        self.deaths = pg.sprite.Group()
        #goals is the group for the goal platform
        self.goals = pg.sprite.Group()
        #platforms is the group for all the non-goal platforms
        self.platforms = pg.sprite.Group()
        #establishes the goal sprite that is the goal of the game
        goal = Platform(ORANGE, WIDTH/2, 100, 75, 20, 0, 0)
        self.all_sprites.add(goal)
        self.goals.add(goal)
        self.boards.add(goal)
        #establishes and defines the player in the game itself
        self.player = Player(self)
        self.all_sprites.add(self.player)
        #establishes the ground
        ground = Platform(GREEN,0, HEIGHT-40, WIDTH, 40, 0, 0)
        self.all_sprites.add(ground)
        self.platforms.add(ground)
        self.boards.add(ground)
        #for loop that populates n number of platforms that are safe and add them to all the various groups
        for x in range(0,5):
            x = Platform(BLUE, rand.randint(100,400),rand.randint(150,500), rand.randint(50, WIDTH-100), rand.randint(10, 40), rand.randint(0,5), 0 )
            self.all_sprites.add(x)
            self.platforms.add(x)
            self.boards.add(x)
        '''second for loop that adds these platforms with RED as the coloration to the death group, thereby creating a difference between the two platform
        despite both being in the same class - sort of a sub-class without creating a new class'''
        for x in range(0,3):
            x = Platform(RED, rand.randint(100,400),rand.randint(150,500), rand.randint(50, WIDTH-100), rand.randint(10, 40), rand.randint(0,5), 0 )
            self.all_sprites.add(x)
            self.deaths.add(x)
            self.platforms.add(x)
            self.boards.add(x)
        
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
        gameOver = pg.sprite.spritecollide(self.player, self.deaths, False)
        
        if hits:
            #happens before the bounce off the bottom to make the game even harder 
            if gameOver:
                print("You lost")
                self.playing = False
                pg.quit
            #This code was copied from Mr. Cozort's test file with slight alteration for the location
            #Code essentially states that if the player sprite's top location blurs into the position of the platform sprite, set velocity to go downard and relocate the sprite to the bottom
            elif self.player.rect.top > hits[0].rect.top:
                self.player.vel.y = 15
                self.player.rect.top = hits[0].rect.bottom + 5
            else:
                self.player.vel.y = 0
                self.player.pos.y = hits[0].rect.top-20
        # if hits and self.player.pos.y == hits[0].rect.bottom:
        #     self.player.vel.y = -self.player.vel.y
        win = pg.sprite.spritecollide(self.player, self.goals, False)
        if win:
            #same logic of hitting the bottom
            if self.player.rect.top > win[0].rect.top:
                self.player.vel.y = 15
                self.player.rect.top = win[0].rect.bottom +5
            #same landing spot but different stuff after that
            else:
                self.player.vel.y = 0
                self.player.pos.y = win[0].rect.top-20
                #sets self.playing to false to reset the game
                print("You win the game")
                self.playing = False
                #ends the game and basically sets to new game
                pg.quit
            

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