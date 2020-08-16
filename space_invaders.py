import pygame
from pygame.sprite import Group
from settings import Settings
from ship import Ship
from alien import Alien
from stars import Star
from game_stats import GameStats
import game_functions as gf

def run_game():
    '''Initialize game an create a new score'''
    pygame.init()
    ai_settings=Settings()
    screen=pygame.display.set_mode((ai_settings.screen_width , ai_settings.screen_height))
    pygame.display.set_caption('Space invaders')
    ship=Ship(ai_settings,screen)
    bullets=Group()
    aliens=Group()
    alien=Alien(ai_settings,screen)
    stars=Group()
    gf.create_fleet(ai_settings,screen,ship,aliens)
    stars=gf.create_stars(ai_settings,screen,stars)
    stats=GameStats(ai_settings)
    while True:
        gf.check_events(ai_settings,screen,ship,bullets)
        if stats.game_active:
            ship.update()
            gf.update_aliens(ai_settings,stats,screen,aliens,ship,bullets)
            gf.update_bullets(ai_settings,screen,ship,bullets,aliens)
        gf.update_screen(ai_settings,screen,ship,bullets,aliens,stars)
run_game()