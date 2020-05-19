###This file was altered/created by: Akshaj Dwivedula

# KidsCanCode - Game Development with Pygame video series
# Jumpy! (a platform game) - Part 2 and Part 5
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
        newspawns = ''
        self.all_sprites = Group()
        #boards is the general group for all non-player sprites
        self.boards = pg.sprite.Group()
        #deaths is the group for the "lava" platforms
        self.safes = pg.sprite.Group()
        self.deaths = pg.sprite.Group()
        self.health = pg.sprite.Group()
        #platforms is the group for all the non-goal platforms
        self.platforms = pg.sprite.Group()
        #establishes the goal sprite that is the goal of the game
        #establishes and defines the player in the game itself
        self.player = Player(self)
        self.all_sprites.add(self.player)
        #establishes the ground
        ground = Platform(GREEN,0, HEIGHT-40, WIDTH, 40, 0, 0)
        print(self.player.health)
        self.all_sprites.add(ground)
        self.platforms.add(ground)
        self.boards.add(ground)
        #group that exists for the algorithm 
        self.tempGroup = Group()
        #creates 5 initial platforms
        for x in range(0,5):
            if len(self.platforms) < 1:
                x = Platform(BLUE, rand.randint(100,400),rand.randint(150,500), rand.randint(50, WIDTH-100), rand.randint(10, 40), rand.randint(0,5), 0 )
                self.all_sprites.add(x)
                self.safes.add(x)
                self.platforms.add(x)
                self.boards.add(x)
            #this algorithm was taken from Mr. Cozort's test file - it essentially adds the created platform in a temp group while testing if it will collide with existing sprites and platforms. 
            # It then removes it from the tempGroup and adds it to the actual platforms
            while True:
                x = Platform(BLUE, rand.randint(100,400),rand.randint(150,500), rand.randint(50, WIDTH-100), rand.randint(10, 40), rand.randint(0,5), 0 )
                self.tempGroup.add(x)
                #checks for collisions for between the newly created platform and exisiting platforms
                selfCollide = pg.sprite.groupcollide(self.tempGroup, self.platforms, True, False)
                allCollide = pg.sprite.groupcollide(self.tempGroup, self.all_sprites, True, False)
                #if no collisions happen (they are away from each other), then can be added
                if not selfCollide and not allCollide:
                    self.platforms.add(x)
                    self.all_sprites.add(x)
                    self.boards.add(x)
                    self.safes.add(x)
                    self.tempGroup.remove(x)
                    break
        
        
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
        if self.player.rect.top <= HEIGHT / 4:
            self.player.pos.y += abs(self.player.vel.y)  
            for plat in self.platforms:
                plat.rect.y += abs(self.player.vel.y)
                if plat.rect.top >= HEIGHT:
                    plat.kill()
        
        ##spawn new platforms

        while len(self.platforms) < 8:
            if len(self.safes) < 3:
                plat = Platform(BLUE, rand.randint(100,400),rand.randint(int(self.player.pos.y) - 30,int(self.player.pos.y)), rand.randint(50, WIDTH-100), rand.randint(10, 40), rand.randint(0,5), 0 )
                self.tempGroup.add(plat)
                selfCollide = pg.sprite.groupcollide(self.tempGroup, self.platforms, True, False)
                #same as before for the algorithm
                if not selfCollide:
                    self.platforms.add(plat)
                    self.all_sprites.add(plat)
                    self.boards.add(plat)
                    self.safes.add(plat)
                    self.tempGroup.remove(plat)
                    break   
            elif len(self.deaths) < 3:
                plat = Platform(RED, rand.randint(100,400),rand.randint(int(self.player.pos.y) - 30,int(self.player.pos.y)), rand.randint(50, WIDTH-100), rand.randint(10, 40), rand.randint(0,5), 0 )
                self.tempGroup.add(plat)
                selfCollide = pg.sprite.groupcollide(self.tempGroup, self.platforms, True, False)
                allCollide = pg.sprite.groupcollide(self.tempGroup, self.all_sprites, True, False)
                #same as before
                if not selfCollide and not allCollide:
                    self.platforms.add(plat)
                    self.all_sprites.add(plat)
                    self.boards.add(plat)
                    self.deaths.add(plat)
                    self.tempGroup.remove(plat)
                    break
            else:
                x = rand.randint(0,2)
                #sets up random platform generation after enough of the first two by associating number with color (color creates a subcass)
                if x == 0:
                    plat = Platform(RED, rand.randint(100,400),rand.randint(int(self.player.pos.y) - 30,int(self.player.pos.y)), rand.randint(50, WIDTH-100), rand.randint(10, 40), rand.randint(0,5), 0 )
                    self.tempGroup.add(plat)
                    selfCollide = pg.sprite.groupcollide(self.tempGroup, self.platforms, True, False)
                    allCollide = pg.sprite.groupcollide(self.tempGroup, self.all_sprites, True, False)
                    if not selfCollide and not allCollide:
                        self.platforms.add(plat)
                        self.all_sprites.add(plat)
                        self.boards.add(plat)
                        self.deaths.add(plat)
                        self.tempGroup.remove(plat)
                        break
                if x == 1:
                    plat = Platform(BLUE, rand.randint(100,400),rand.randint(int(self.player.pos.y) - 30,int(self.player.pos.y)), rand.randint(50, WIDTH-100), rand.randint(10, 40), rand.randint(0,5), 0 )
                    self.tempGroup.add(plat)
                    selfCollide = pg.sprite.groupcollide(self.tempGroup, self.platforms, True, False)
                    allCollide = pg.sprite.groupcollide(self.tempGroup, self.all_sprites, True, False)
                    if not selfCollide and not allCollide:
                        self.platforms.add(plat)
                        self.all_sprites.add(plat)
                        self.boards.add(plat)
                        self.safes.add(plat)
                        self.tempGroup.remove(plat)
                        break 
                if x == 2:
                    plat = Platform(GREEN, rand.randint(100,400),rand.randint(int(self.player.pos.y) - 30,int(self.player.pos.y)), 10, 10, 0, 0 )
                    self.tempGroup.add(plat)
                    selfCollide = pg.sprite.groupcollide(self.tempGroup, self.platforms, True, False)
                    allCollide = pg.sprite.groupcollide(self.tempGroup, self.all_sprites, True, False)
                    if not selfCollide and not allCollide:
                        self.platforms.add(plat)
                        self.all_sprites.add(plat)
                        self.boards.add(plat)
                        self.health.add(plat)
                        self.tempGroup.remove(plat)
                        break  

        hits = pg.sprite.spritecollide(self.player, self.platforms, False)
        gameOver = pg.sprite.spritecollide(self.player, self.deaths, False)
        restock = pg.sprite.spritecollide(self.player, self.health, False)

        if hits:
            #happens before the bounce off the bottom to make the game even harder 
            if gameOver:
                print("You lost")
                self.playing = False
                pg.quit
            #special color has certain benefits 
            if restock:
                self.player.health = 100
                print("Health Restored! ")
            #This code was copied from Mr. Cozort's test file with slight alteration for the location
            #Code essentially states that if the player sprite's top location blurs into the position of the platform sprite, set velocity to go downard and relocate the sprite to the bottom
            elif self.player.rect.top > hits[0].rect.top:
                self.player.health = self.player.health - 10
                print("Your health is " + str(self.player.health))
                self.player.vel.y = 15
                self.player.rect.top = hits[0].rect.bottom + 5
            else:
                self.player.vel.y = 0
                self.player.pos.y = hits[0].rect.top-20
        if self.player.health == 0:
            print("You lost")
            self.player = False
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