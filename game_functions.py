import pygame
import sys
from pygame.locals import *
from pygame_learning.bullet import Bullet

def check_keydown_events(event,ship):
    if event.key== pygame.K_RIGHT:
        ship.moving_right = True
    elif event.key== pygame.K_LEFT:
        ship.moving_left = True
    elif event.key == pygame.K_q:
        sys.exit()

def check_keyup_events(event,ship):
    if event.key== pygame.K_RIGHT:
        ship.moving_right = False
    elif event.key== pygame.K_LEFT:
        ship.moving_left = False

def check_events(ship):
    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            sys.exit()
        elif event.type==pygame.KEYDOWN:
            check_keydown_events(event,ship)
        elif event.type==pygame.KEYUP:
            check_keyup_events(event,ship)


def fire_bullets(settings,screen,ship,bullets):
    if settings.bullet_nowcount==0:
        new_bullet=Bullet(settings,screen,ship)
        bullets.add(new_bullet)
        settings.bullet_nowcount=settings.bullet_fre
    else:
        settings.bullet_nowcount-=1
    for bullet in bullets.copy():
        if bullet.rect.bottom<screen.get_rect().top:
            bullets.remove(bullet)
    print(len(bullets))

def update_screen(settings,screen,ship,bullets):
    screen.fill(settings.bg_color)
    ship.blitme()
    for bullet in bullets.sprites():
        bullet.blitme()
    pygame.display.flip()

