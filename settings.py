# made by wangzhi
# TX_Leo

class Settings:
    '''存储游戏《外星人入侵》中所有设置的类'''
    def __init__(self):
        '''初始化游戏的静态设置'''

        #屏幕设置
        self.screen_width=1080
        self.screen_height=800#页面大小设置
        self.bg_color=(0,0,0)#背景颜色设置,三元色

        #飞船设置
        self.ship_speed=0.1#飞船速度设置
        self.ship_limit=3#设置飞船的个数

        #子弹设置
        self.bullet_speed=0.5#子弹速度
        self.bullet_width=3#子弹宽度（子弹是一个矩形）
        self.bullet_height=30#子弹长度
        self.bullet_color=(255,255,255)#子弹颜色
        self.bullets_allowed=5#设置子弹一次性最多的数量

        #外星人设置
        self.alien_speed=3#一个外星人的速度
        self.fleet_drop_speed=15#外星人舰队的速度
        #fleet_direction 为1表示向右移，为-1表示向左移
        self.fleet_direction=1

        #加快游戏节奏的速度
        self.speedup_scale=1.2

        #外星人分数的提高速度
        self.score_scale=1.5

        self.initialize_dynamic_settings()

    def initialize_dynamic_settings(self):
        '''初始化随游戏进行而变化的设置'''

        self.ship_speed=1.0
        self.bullet_speed=3.0
        self.alien_speed=1.0

        #fleet_direction为1表示向右，为-1表示向左
        self.fleet_direction=1

        #记分
        self.alien_points=50

    def increase_speed(self):
        '''提高速度设置和外星人分数'''

        self.ship_speed*=self.speedup_scale
        self.bullet_speed*=self.speedup_scale
        self.alien_speed*=self.speedup_scale
        self.alien_points=int(self.alien_points*self.speedup_scale)
        print(self.alien_points)