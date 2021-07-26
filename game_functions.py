# made by wangzhi
# TX_Leo
import sys
import pygame
from bullet import Bullet
from alien import Alien
from time import sleep


def __init__(self):
    '''初始化游戏并创建资源'''
    pygame.init()  # 初始化背景设置

    self.settings = Settings()  # 创建Settings的实例对象

    self.screen = pygame.display.set_mode(
        (self.settings.screen_width, self.settings.screen_height))  # 创建显示窗口，宽1200像素，高800像素

    pygame.display.set_caption("Alien Invasion")  # 设置游戏的名字

    self.bg_color = (230, 230, 230)  # 设置背景颜色

    # 创建存储游戏统计信息的实例，并创建记分牌
    self.stats = GameStats(self)  # 创建一个用于存储游戏统计信息的实例
    self.sb = Scoreboard(self)

    self.ship = Ship(self)  # 创建ship实例对象

    self.bullets = pygame.sprite.Group()  # 创建用于存储子弹的编组

    self.aliens = pygame.sprite.Group()  # 创建用于存储外星人的编组

    self._creat_fleet()  # 创建外星人群

    self.play_button = Button(self, "Play")  # 创建按钮的实例对象


def run_game(self):
    '''开始游戏的主循环'''

    while True:
        '''每次都重绘屏幕'''
        self._check_events()

        # 如果是活跃状态
        if self.stats.game_active:
            '''运行持续运动'''
            self.ship.update()

            '''更新子弹的位置并删除子弹'''
            self._update_bullets()

            '''更新每个外星人的位置'''
            self._update_aliens()

        '''更新屏幕上的图像，并切换到新屏幕'''
        self._update_screen()


def _check_events(self):
    '''响应按键和鼠标事件'''

    for event in pygame.event.get():  # 访问pygame检测到的事件，返回一个列表
        if event.type == pygame.QUIT:  # 单机游戏关闭按钮
            sys.exit()  # 就退出了

        elif event.type == pygame.KEYDOWN:  # 检测到有KEYDOWN行为（按键）
            self._check_keydown_events(event)

        elif event.type == pygame.KEYUP:  # 检测到有KEYUP行为（松键）
            self._check_keyup_events(event)

        elif event.type == pygame.MOUSEBUTTONDOWN:  # 检测有鼠标行为
            mouse_pos = pygame.mouse.get_pos()
            self._check_play_button(mouse_pos)


def _check_keydown_events(self, event):
    '''响应按键'''

    # 向右移动飞船
    if event.key == pygame.K_RIGHT:  # 如果是右键箭头
        self.ship.moving_right = True

    # 向左移动飞船
    elif event.key == pygame.K_LEFT:
        self.ship.moving_left = True

    # 按动Q键就会退出（quit）
    elif event.key == pygame.K_q:
        sys.exit()

    # 空格键开火
    elif event.key == pygame.K_SPACE:
        self._fire_bullet()

    # p键开始游戏
    elif event.key == pygame.K_p:
        self._start_game()


def _check_keyup_events(self, event):
    '''响应松开'''

    # 如果松开右键
    if event.key == pygame.K_RIGHT:
        self.ship.moving_right = False

    # 如果松开左键
    elif event.key == pygame.K_LEFT:
        self.ship.moving_left = False


def _check_play_button(self, mouse_pos):
    '''玩家单击Play按钮时开始游戏'''

    button_clicked = self.play_button.rect.collidepoint(mouse_pos)
    if button_clicked and not self.stats.game_active:
        self._start_game()


def _start_game(self):
    '''游戏开始'''

    # 重置游戏统计信息
    self.stats.reset_stats()
    self.stats.game_active = True  # 重新改变游戏状态
    self.sb.prep_score()  # 重新改变记分器
    self.sb.prep_level()  # 重新改变等级
    self.sb.prep_ships()  # 重新改变剩余的飞船数

    # 清空余下的外星人和子弹
    self.aliens.empty()
    self.bullets.empty()

    # 创建一群新的外星人并让飞船居中
    self._creat_fleet()
    self.ship.center_ship()

    # 隐藏鼠标光标
    pygame.mouse.set_visible(False)

    # 重置游戏设置
    self.settings.initialize_dynamic_settings()


def _fire_bullet(self):
    '''创建子弹，并将其加入编组bullets中'''

    if len(self.bullets) < self.settings.bullets_allowed:  # 限制子弹数量
        new_bullet = Bullet(self)
        self.bullets.add(new_bullet)


def _update_screen(self):
    '''监视键盘和鼠标事件'''

    self.screen.fill(self.settings.bg_color)  # 每次循环时都重绘屏幕
    self.ship.blitme()  # 将飞船绘制到屏幕上
    for bullet in self.bullets.sprites():
        bullet.draw_bullet()
    self.aliens.draw(self.screen)

    # 显示得分
    self.sb.show_score()

    # 如果游戏处于非活动状态，就绘制Play按钮
    if not self.stats.game_active:
        self.play_button.draw_button()

    '''让最近绘制的屏幕可见'''
    pygame.display.flip()


def _update_bullets(self):
    '''更新子弹的位置并删除消失的子弹'''

    # 更新子弹的位置
    self.bullets.update()

    # 删除消失的子弹
    for bullet in self.bullets.copy():
        if bullet.rect.bottom <= 0:
            self.bullets.remove(bullet)  # 如果跳出这个屏幕就删去
    self._check_bullet_alien_collision()


def _check_bullet_alien_collision(self):
    '''响应子弹外星人碰撞'''

    # 删除发生碰撞的子弹和外星人
    collisions = pygame.sprite.groupcollide(self.bullets, self.aliens, True, True)

    # 记分
    if collisions:
        for aliens in collisions.values():
            self.stats.score += self.settings.alien_points * len(aliens)
            self.sb.prep_score()
            self.sb.check_high_score()

    # 删除现有的子弹并新建一群外星人
    if not self.aliens:
        self.bullets.empty()
        self._creat_fleet()
        self.settings.increase_speed()

        # 提高等级
        self.stats.level += 1
        self.sb.prep_level()


def _creat_fleet(self):
    '''创建外星人群'''

    # 外星人的间距为外星人宽度
    alien = Alien(self)  # 创建Alien实例对象
    alien_width, alien_height = alien.rect.size

    # 计算可用于放置外星人的水平空间以及其中可容纳多少个外星人
    available_space_x = self.settings.screen_width - (2 * alien_width)
    number_aliens_x = available_space_x // (2 * alien_width)

    # 计算屏幕可容纳多少行外星人
    ship_height = self.ship.rect.height
    available_space_y = (self.settings.screen_height -
                         (3 * alien_height) - ship_height)
    number_rows = available_space_y // (2 * alien_height)

    # 创建外星人群
    for row_number in range(number_rows):
        for alien_number in range(number_aliens_x):  # 编写一个循环，从零数到要创建的外星人的数
            self._creat_alien(alien_number, row_number)


def _creat_alien(self, alien_number, row_number):
    '''创建一个外星人并将其放在当前行'''

    alien = Alien(self)

    # 设置外星人大小
    alien_width, alien_height = alien.rect.size
    alien.x = alien_width + 2 * alien_width * alien_number
    alien.rect.x = alien.x
    alien.rect.y = alien.rect.height + 2 * alien.rect.height * row_number
    self.aliens.add(alien)  # 加到外星人编组中


def _update_aliens(self):
    '''检查是否所有外星人位于屏幕边缘
    更新外星人群中所有外星人的位置'''

    self._check_fleet_edges()
    self.aliens.update()

    # 检测外星人和飞船之间的碰撞
    if pygame.sprite.spritecollideany(self.ship, self.aliens):
        self._ship_hit()

    # 检查是否有外星人到达底端
    self._check_aliens_bottom()


def _check_fleet_edges(self):
    '''有外星人到达边缘时采取相应的措施'''

    for alien in self.aliens.sprites():
        if alien.check_edges():
            self._change_fleet_direction()
            break


def _change_fleet_direction(self):
    '''将整群外星人下移，并改变他们的方向'''

    for alien in self.aliens.sprites():
        alien.rect.y += self.settings.fleet_drop_speed
    self.settings.fleet_direction *= -1


def _ship_hit(self):
    '''响应飞船被外星人撞到'''

    if self.stats.ships_left > 0:

        # 将ship_left减1并更新记分牌
        self.stats.ships_left -= 1
        self.sb.prep_ships()

        # 清空余下的外星人和子弹
        self.aliens.empty()
        self.bullets.empty()

        # 创建一群新的外星人，并将飞船放到屏幕底端的中央
        self._creat_fleet()
        self.ship.center_ship()

        # 暂停
        sleep(0.5)

    else:
        self.stats.game_active = False
        pygame.mouse.set_visible(True)  # 鼠标光标可见


def _check_aliens_bottom(self):
    '''检查是否有外星人到达了屏幕底端'''
    screen_rect = self.screen.get_rect()
    for alien in self.aliens.sprites():
        if alien.rect.bottom >= screen_rect.bottom:
            # 像飞船被撞到一样处理
            self._ship_hit()
            break