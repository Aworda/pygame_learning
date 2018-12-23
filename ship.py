import pygame

class Ship():
    def __init__(self,screen,settings):
        self.screen=screen
        self.image=pygame.image.load('image/ship.bmp')
        self.rect=self.image.get_rect()
        self.screen_rect=screen.get_rect()
        self.settings=settings

        self.rect.centerx=self.screen_rect.centerx  # 屏幕中央
        self.rect.bottom=self.screen_rect.bottom # 屏幕底部
        self.moving_right=False
        self.moving_left=False

    def update(self):
        if self.moving_left and self.rect.left>0:
            self.rect.centerx-=self.settings.ship_speed
        elif self.moving_right and self.rect.right<self.screen_rect.right:
            self.rect.centerx+=self.settings.ship_speed

    def blitme(self):
        self.update()
        self.screen.blit(self.image,self.rect)
