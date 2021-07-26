import sys
import pygame
from time import sleep
from bullets import Bullet
from alien import Alien
from stars import Star

def check_keydown_events(event,ai_settings,screen,ship,bullets):
    '''checks for any keydown event'''
    if event.key==pygame.K_RIGHT:
        ship.moving_right=True
    elif event.key==pygame.K_LEFT:
        ship.moving_left=True

    if event.key==pygame.K_DOWN:
        ship.moving_down=True
    elif event.key==pygame.K_UP:
        ship.moving_up=True

    if event.key==pygame.K_SPACE:
        fire_bullets(ai_settings,screen,ship,bullets)

    elif event.key==pygame.K_q:
        pygame.quit()
        sys.exit()

def check_keyup_events(event,ai_settings,screen,ship,bullets):
        '''check for any keyup event'''
        if event.key==pygame.K_RIGHT:
            ship.moving_right=False
        elif event.key==pygame.K_LEFT:
            ship.moving_left=False

        if event.key==pygame.K_DOWN:
            ship.moving_down=False
        elif event.key==pygame.K_UP:
            ship.moving_up=False

def check_events(ai_settings,screen,ship,bullets):
    '''Check if there's an event in a given moment'''
    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            pygame.quit()
            sys.exit()

        elif event.type==pygame.KEYDOWN:
            check_keydown_events(event,ai_settings,screen,ship,bullets)

        elif event.type==pygame.KEYUP:
            check_keyup_events(event,ai_settings,screen,ship,bullets)

def update_screen(ai_settings,screen,ship,bullets,aliens,stars):
    '''Update images newly draw in the screen'''
    screen_rect=screen.get_rect()
    screen.fill((ai_settings.bg_color))
    for star in stars.sprites():
        star.update()
        if star.rect.bottom==screen_rect.bottom:
            star.y=0
        star.blitme()
    ship.blitme()
    aliens.draw(screen)
    for bullet in bullets.sprites():
        bullet.blitme()
    pygame.display.flip()

def update_bullets(ai_settings,screen,ship,bullets,aliens):
    '''Update the position of the bullets and remove old bullets'''
    bullets.update()
    for bullet in bullets.copy():
        if bullet.rect.bottom==0:
            bullets.remove(bullet)
    collisions=pygame.sprite.groupcollide(bullets,aliens,True,True)
    if len(aliens)==0:
        bullets.empty()
        create_fleet(ai_settings,screen,ship,aliens)
        ai_settings.fleet_drop_speed+=5

def fire_bullets(ai_settings,screen,ship,bullets):
    '''Fire bullets if limit not reached yet'''
    if len(bullets)<ai_settings.bullets_allowed:
        new_bullet=Bullet(ai_settings,screen,ship)
        bullets.add(new_bullet)

def get_number_aliens_x(ai_settings,alien_width):
    '''Determine the number of aliens that will fit in a row.'''
    available_space_x=ai_settings.screen_width-2*alien_width
    return int(available_space_x/(2*alien_width))

def create_alien(ai_settings,screen,aliens,alien_number):
    alien=Alien(ai_settings,screen)
    alien_width=0.75*alien.rect.width
    alien.x=alien_width + 2*alien_width*alien_number
    alien.rect.x=alien.x
    aliens.add(alien)

def create_fleet(ai_settings,screen,ship,aliens):
    '''Create a full fleet of aliens.'''
    alien=Alien(ai_settings,screen)
    number_aliens_x=get_number_aliens_x(ai_settings,0.75*alien.rect.width)
    for alien_number in range(number_aliens_x):
        create_alien(ai_settings,screen,aliens,alien_number)

def change_fleet_direction(ai_settings,aliens):
    '''Change the direction of the current fleet'''
    for alien in aliens.sprites():
        alien.rect.y+=ai_settings.fleet_drop_speed
    ai_settings.fleet_direction*=-1

def check_fleet_edges(ai_settings,aliens):
    '''Check if the edges of the fleet are touching the edges of the screen,
    and if so, drop the fleet some rows down'''
    for alien in aliens.sprites():
        if alien.check_edges():
            change_fleet_direction(ai_settings,aliens)

def update_aliens(ai_settings,stats,screen,aliens,ship,bullets):
    '''Update the position of the alien fleet'''
    check_fleet_edges(ai_settings,aliens)
    aliens.update()
    if pygame.sprite.spritecollideany(ship,aliens):
        ship_hit(ai_settings,stats,screen,ship,aliens,bullets)
    check_aliens_bottom(ai_settings,stats,screen,ship,aliens,bullets)

def create_stars(ai_settings,screen,stars):
    for _ in range(ai_settings.stars_number):
        star=Star(ai_settings,screen)
        stars.add(star)
    return stars

def ship_hit(ai_settings,stats,screen,ship,aliens,bullets):
    '''What to do if a ship gets hit by an alien'''
    if stats.ships_left>0:
        stats.ships_left-=1
        aliens.empty()
        bullets.empty()
        create_fleet(ai_settings,screen,ship,aliens)
        ship.center_ship()
        sleep(0.5)
    else:stats.game_active=False

def check_aliens_bottom(ai_settings,stats,screen,ship,aliens,bullets):
    '''Check if any aliens have reached the bottom of the screen.'''
    screen_rect=screen.get_rect()
    for alien in aliens.sprites():
        if alien.rect.bottom>=screen_rect.bottom:
            ship_hit(ai_settings,stats,screen,ship,aliens,bullets)
            break