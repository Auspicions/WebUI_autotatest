import pygame
class ShenTi:
    def __init__(self,screen,x,y):
        self.x =x
        self.y =y
        self.shenti = pygame.image.load("picture/shenti.gif").convert()
        self.screen = screen
    def display(self):
        self.screen.blit (self.shenti,(self.x, self.y))
    def genSui(self,x):
        self.x=x
