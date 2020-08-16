import pygame
from pygame.sprite import Sprite

class Bullet(Sprite):
    '''The class for the bullets'''
    def __init__(self,ai_settings,screen,ship):
        super(Bullet,self).__init__()
        '''Initialize bullet class as a subclass of the superclass Sprite.'''
        self.screen=screen

        self.rect=pygame.Rect(0,0,ai_settings.bullet_width,ai_settings.bullet_height)
        self.rect.centerx=ship.rect.centerx
        self.rect.top=ship.rect.top
        self.y=float(self.rect.y)
        self.color=ai_settings.bullet_color
        self.speed=ai_settings.bullet_speed

    def update(self):
        '''Computes the new position of the bullets'''
        self.y-=self.speed
        self.rect.y=self.y

    def blitme(self):
        '''Draw the bullet at its current location'''
        pygame.draw.rect(self.screen, self.color, self.rect)