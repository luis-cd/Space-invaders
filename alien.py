import pygame
from pygame.sprite import Sprite

class Alien(Sprite):
    '''The alien class'''
    def __init__(self, ai_settings,screen):
        super(Alien,self).__init__()
        '''Initialize alien class as a subclass of the superclass Sprite.'''
        
        #load alien and get its rect
        self.ai_settings=ai_settings
        self.screen= screen
        self.image=pygame.image.load('images/alien.bmp')
        self.rect=self.image.get_rect()

        #put the alien in the upper left corner
        self.rect.x=self.rect.width
        self.rect.y=self.rect.height
        self.x=float(self.rect.x)
        
    def check_edges(self):
        '''return True if the alien is at edge of screen'''
        self.screen_rect=self.screen.get_rect()
        if self.rect.right==self.screen_rect.right or self.rect.left==0:
            return True


    def update(self):
        '''update alien position'''
        self.x+=self.ai_settings.alien_speed*self.ai_settings.fleet_direction
        self.rect.x=self.x