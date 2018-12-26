import pygame
import sys
from pygame.locals import *
from pygame_learning.bullet import Bullet
from pygame_learning.Alien import Alien

def creat_fleet(settings,screen,aliens):
    alien=Alien(settings,screen)
    alien_width=alien.rect.width
    available_space_x=settings.screen_width-2*alien_width
    number_aliens_x=int(available_space_x/(2*alien_width))

    for alien_number in range(number_aliens_x):
        alien=Alien(settings,screen)
        alien.x=alien_width+2*alien_width*alien_number
        alien.rect.x=alien.x
        aliens.add(alien)

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

def check_events(ship,play_button,settings):
    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            sys.exit()
        if event.type==pygame.KEYDOWN:
            check_keydown_events(event,ship)
        elif event.type==pygame.KEYUP:
            check_keyup_events(event,ship)
        if event.type==pygame.MOUSEBUTTONDOWN:
            mouse_x,mouse_y=pygame.mouse.get_pos()
            if play_button.rect.collidepoint(mouse_x,mouse_y):
                settings.game_active=True


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
    #print(len(bullets))

def update_screen(settings,screen,aliens,ship,bullets,play_button,sb):
    screen.fill(settings.bg_color)
    if settings.game_active:
        ship.blitme()
        aliens.draw(screen)
        sb.show_score()
        pygame.mouse.set_visible(False)
        for bullet in bullets.sprites():
            bullet.blitme()
    else:
        play_button.draw_button()
    pygame.display.flip()

def update_bullets(aliens,bullets,sb):
    collisions=pygame.sprite.groupcollide(bullets,aliens,True,True)
    for collision in collisions.values():
        sb.score+=len(collision)
        sb.prep_score(sb.score)

