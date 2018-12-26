import pygame
import sys
from pygame_learning.settings import Settings
from pygame_learning.ship import Ship
from pygame_learning.bullet import Bullet
import pygame_learning.game_functions as gf
from pygame.sprite import Group
from pygame_learning.button import Button
from pygame_learning.Alien import Alien
from pygame_learning.scoreboard import Score_board


def run_game():
    pygame.init()
    settings = Settings()
    screen = pygame.display.set_mode((settings.screen_width, settings.screen_height), 0, 32)  # 窗口模式为0，全屏模式为FULLSCREEN
    ship = Ship(screen,settings)
    aliens=Group()
    gf.creat_fleet(settings,screen,aliens)
    bullets=Group()
    sb=Score_board(settings,screen,settings.score)
    play_button=Button(settings,screen,"Play")
    pygame.display.set_caption("Alien Invasion")
    while True:
        gf.check_events(ship,play_button,settings)
        if settings.game_active:
            #ship.update()
            gf.fire_bullets(settings, screen, ship, bullets)
            gf.update_bullets(aliens,bullets,sb)
        else:
            pass
        gf.update_screen(settings, screen, aliens, ship, bullets,play_button,sb)
run_game()
