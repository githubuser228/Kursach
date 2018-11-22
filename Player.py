import pygame
from Constants import *
from pygame.locals import *
class Player():

    def __init__(self,name):

        self.state = ALIVE
        self.direction = UP
        self.x = START_X
        self.y = START_Y
        self.name = name
        self.hp = MAX_HP
        self.mp = MAX_MP
        self.image_pack = ['data/playerr.png', 'data/playerd.png', 'data/playerl.png', 'data/playeru.png']
        self.images = []
        for image in self.image_pack:
            temp = pygame.image.load(image).convert_alpha()
            i = []
            i.append(temp.subsurface(0,0,64,64))
            i.append(temp.subsurface(64, 0, 64, 64))
            i.append(temp.subsurface(128, 0, 64, 64))
            self.images.append(i)

        self.mooving=[0,0,0,0]

    def moove(self):
        if self.mooving[RIGHT] == 1:
            self.x += PLAYER_SPEED
        if self.mooving[DOWN] == 1:
            self.y += PLAYER_SPEED
        if self.mooving[LEFT] == 1:
            self.x -= PLAYER_SPEED
        if self.mooving[UP] == 1:
            self.y -= PLAYER_SPEED


    def render(self, screen):
        screen.blit(self.images[self.direction][self.state], (self.x,self.y))

    def render_ui(self,screen):
        pass