import pygame
class Score_board():
    def __init__(self,settings,screen,score):
        self.screen=screen
        self.screen_rect=screen.get_rect()
        self.text_color=(30,30,30)
        self.font = pygame.font.Font("GB2312.ttf", 48)
        self.settings=settings
        self.score=int(score)
        self.prep_score(self.score)

    def prep_score(self,score):
        self.msg_image=self.font.render(str(score),True,self.text_color,self.settings.bg_color)
        self.msg_image_rect=self.msg_image.get_rect()
        self.msg_image_rect.right=self.screen_rect.right-20
        self.msg_image_rect.top=20

    def show_score(self):
        self.screen.blit(self.msg_image,self.msg_image_rekct)