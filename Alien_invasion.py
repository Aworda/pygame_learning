import pygame
import sys
from pygame_learning.settings import Settings
from pygame_learning.ship import Ship
from pygame_learning.bullet import Bullet
import pygame_learning.game_functions as gf
from pygame.sprite import Group


def run_game():
    pygame.init()
    settings = Settings()
    screen = pygame.display.set_mode((settings.screen_width, settings.screen_height), 0, 32)  # 窗口模式为0，全屏模式为FULLSCREEN
    ship = Ship(screen,settings)
    bullets=Group()
    pygame.display.set_caption("Alien Invasion")
    while True:
        gf.check_events(ship)
        #ship.update()
        gf.fire_bullets(settings, screen, ship, bullets)
        gf.update_screen(settings,screen,ship,bullets)

run_game()
