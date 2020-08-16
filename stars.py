import pygame
import random as rd
from pygame.sprite import Sprite

class Star(Sprite):
    '''Class for the star decoration'''
    def __init__(self, ai_settings,screen):
        super(Star,self).__init__()
        '''Initialize alien class as a subclass of the superclass Sprite.'''

        self.ai_settings=ai_settings
        self.screen=screen
        self.image=pygame.image.load('images/stars.bmp')
        self.rect=self.image.get_rect()

        self.rect.x=rd.uniform(0,ai_settings.screen_width)
        self.rect.y=rd.uniform(0,ai_settings.screen_height)
        self.y=float(self.rect.y)

    def update(self):
        '''Update the position of the stars'''
        self.y+=self.ai_settings.star_speed
        self.rect.y=self.y
    
    def blitme(self):
        '''Draw the star at its current location'''
        self.screen.blit(self.image, self.rect)