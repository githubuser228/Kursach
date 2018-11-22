import pygame
from Constants import *
from Player import *
from pygame.locals import *

class Main():
    def __init__(self, screen):
        self.screen = screen
        self.player = Player('Test')
        self.background = pygame.image.load('data/background.jpg')
        self.running = True
        self.main_loop()

    def handle_events(self):
        for event in pygame.event.get():
            if event.type == QUIT:
                self.running = False
            #ПЕРДВЕЖЕНИЕ ИГРОКА
            elif event.type == KEYDOWN:
                if event.key == K_RIGHT:
                    self.player.direction = RIGHT
                    self.player.mooving = [1,0,0,0]
                if event.key == K_DOWN:
                    self.player.direction = DOWN
                    self.player.mooving = [0,1,0,0]
                if event.key == K_LEFT:
                    self.player.direction = LEFT
                    self.player.mooving = [0,0,1,0]
                if event.key == K_UP:
                    self.player.direction = UP
                    self.player.mooving = [0,0,0,1]
            elif event.type == KEYUP:
                if event.key == K_UP:
                    self.player.mooving[UP] = 0
                if event.key == K_DOWN:
                    self.player.mooving[DOWN] = 0
                if event.key == K_RIGHT:
                    self.player.mooving[RIGHT] = 0
                if event.key == K_LEFT:
                    self.player.mooving[LEFT] = 0


    def render (self):
        self.screen.blit(self.background,(0,0))
        self.player.render(screen)
        pygame.display.flip()

    def main_loop(self):
        while self.running == True:
            self.player.moove()
            self.render()
            self.handle_events()

pygame.init()
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
game = Main(screen)