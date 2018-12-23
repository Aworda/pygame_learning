import pygame
from pygame.sprite import Sprite

class Bullet(Sprite):
    def __init__(self,settings,screen,ship):
        super().__init__()
        self.screen=screen

        self.rect=pygame.Rect(0,0,settings.bullet_width,settings.bullet_height)
        self.rect.centerx=ship.rect.centerx
        self.rect.top=ship.rect.top
        self.y=float(self.rect.y)
        self.color=settings.bullet_color
        self.speed=settings.bullet_speed
        self.screen_rect = screen.get_rect()

    def update(self):
        self.y-=self.speed
        self.rect.y=self.y

    def blitme(self):
        self.update()
        if self.rect.y>self.screen_rect.top:
            pygame.draw.rect(self.screen,self.color,self.rect)