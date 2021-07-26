# made by wangzhi
# TX_Leo
import pygame
from pygame.sprite import  Sprite
from settings import Settings

class BlackHole(Sprite):

    def __init__(self,ai_game):
        super().__init__()
        self.screen = ai_game.screen
        self.settings = ai_game.settings
        self.screen_rect = ai_game.screen.get_rect()
        '''加载黑洞图像并获取其外接矩形'''
        self.image=pygame.image.load('images/blackhole.jpg')
        self.rect=self.image.get_rect()

        self.rect.y=self.rect.height
        self.rect.x = self.rect.width

        '''在黑洞的属性x中存储小数值'''
        self.x=float(self.rect.x)

    def blitme(self):
        '''在指定位置绘制黑洞'''

        self.screen.blit(self.image, self.rect)

    def update(self):
        '''使黑洞向下移动'''

        self.rect.y += self.settings.fleet_drop_speed
        self.rect.x=self.x

