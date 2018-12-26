class Settings():
    """存储该游戏所有的设置"""
    def __init__(self):
        self.screen_width=1200
        self.screen_height=800
        self.bg_color=(230,230,230)
        self.ship_speed=10
        self.bullet_speed=15
        self.bullet_width=3
        self.bullet_height=10
        self.bullet_color=(60,60,60)
        self.bullet_fre=3
        self.bullet_nowcount=self.bullet_fre
        self.game_active=False
        self.score="0"