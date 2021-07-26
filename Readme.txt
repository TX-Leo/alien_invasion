这是我大一上参加软件设计大赛时的作品，哪个说明文档是我当时上交的
这是一个pygame的典例游戏，假期自学了python之后，在此基础上加了一些改进。
虽然比较简单与基础，但是是我第一个总结写的较大型工程，学习到了很多总体还是非常满意的，甚至还得了个三等奖

#改进：
音效，背景图片，图像优化，等级添加，队形改变（有bug）等
#bug：（队形改变之后外星人会突然某一时刻降落，不知道为什么）
原代码：

    #创建外星人群
    for row_number in range(number_rows):
        for alien_number in range(number_aliens_x):#编写一个循环，从零数到要创建的外星人的数
            self._creat_alien(alien_number,row_number)

def _creat_alien(self,alien_number,row_number):
    '''创建一个外星人并将其放在当前行'''

    alien=Alien(self)

    #设置外星人大小
    alien_width,alien_height=alien.rect.size
    alien.x=alien_width+2*alien_width*alien_number
    alien.rect.x=alien.x
    alien.rect.y=alien.rect.height+2*alien.rect.height*row_number
    self.aliens.add(alien)#加到外星人编组中


改进代码：

    #创建外星人群
    for row_number in range(number_rows):
        for alien_number in range(number_aliens_x-row_number*2):#编写一个循环，从零数到要创建的外星人的数
            self._creat_alien(alien_number,row_number)

def _creat_alien(self,alien_number,row_number):
    '''创建一个外星人并将其放在当前行'''

    alien=Alien(self)

    #设置外星人大小
    alien_width,alien_height=alien.rect.size
    alien.x=2*row_number*alien_width+2*alien_width*alien_number
    alien.rect.x=alien.x+alien_width
    alien.rect.y=alien.rect.height+2*alien.rect.height*row_number
    self.aliens.add(alien)#加到外星人编组中

#还需改进的点：
*让外星人也会发出子弹（火或者别的）
*设置障碍（比如黑洞）
*添加游戏暂停功能，如按某个按键，实现游戏暂停
*最高得分永久性存储，在关闭后，再打开游戏时，仍然可以正常读取和显示
*添加boss，添加血条
*子弹设置为图像
*设置碰撞效果
