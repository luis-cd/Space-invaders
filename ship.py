import pygame

class Ship():
    def __init__(self,ai_settings,screen):
        '''Initialize the ship and set its starting position'''
        self.screen=screen

        #load ship and get its rect (and its settings)
        self.image=pygame.image.load('images/ship.bmp')
        self.rect=self.image.get_rect()
        self.screen_rect=screen.get_rect()
        self.ai_settings=ai_settings

        #center the ship at the beginning of the game.
        self.rect.centerx=self.screen_rect.centerx
        self.rect.bottom=self.screen_rect.bottom

        #atributes of movement for the ship class
        self.moving_right=False
        self.moving_left=False
        self.moving_down=False
        self.moving_up=False
        self.center_xaxis=float(self.rect.centerx) #This you are the same than rect.centerx/y, with the only difference that these store floats, and not ints.
        self.center_yaxis=float(self.rect.centery)

    def update(self):
        '''Update ship position'''
        if self.moving_right and self.rect.right<self.screen_rect.right:
            self.center_xaxis+=self.ai_settings.ship_speed
        elif self.moving_left and self.rect.left>0:
            self.center_xaxis-=self.ai_settings.ship_speed

        if self.moving_up and self.rect.top>0:
            self.center_yaxis-=self.ai_settings.ship_speed
        elif self.moving_down and self.rect.bottom<self.screen_rect.bottom:
            self.center_yaxis+=self.ai_settings.ship_speed

        self.rect.center=(self.center_xaxis,self.center_yaxis)


    def blitme(self):
        '''Draw the ship at its current location.'''
        self.screen.blit(self.image,self.rect)

    def center_ship(self):
        '''Center the ship in the initial position.'''
        self.center_xaxis=float(self.screen_rect.centerx)
        self.center_yaxis=float(self.screen_rect.bottom-20)