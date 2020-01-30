import random

import pygame

# 屏幕常量
SCREEN_RECT = pygame.Rect(0, 0, 480, 700)
# 刷新帧率
SCREEN_FPS = 60
# 敌机出场事件
CREATE_ENEMY_EVENT = pygame.USEREVENT
# 英雄发射子弹事件
HERO_FIRE_EVENT = pygame.USEREVENT + 1


class GameSprite(pygame.sprite.Sprite):
    """精灵类"""

    def __init__(self, image_name, speed=1):
        # 调用父类初始化方法
        super().__init__()
        # 定义对象的属性
        self.image = pygame.image.load(image_name)
        self.rect = self.image.get_rect()
        self.speed = speed

    def update(self, *args):
        self.rect.y += self.speed


class Background(GameSprite):
    """游戏背景精灵"""

    def __init__(self, is_alt=False):
        image_name = "./images/background.png"
        # 1.调用父类方法实现精灵的创建(image/rect/speed)
        super().__init__(image_name)
        # 2.判断是否是交替图像,如果是需要设置初始位置
        if is_alt:
            self.rect.y = - self.rect.height

    def update(self, *args):
        # 1.调用父类的方法实现
        super().update()
        # 2.判断图像是否移出屏幕,如果移出屏幕需要将图像移到屏幕上方
        if self.rect.y >= SCREEN_RECT.height:
            self.rect.y = -self.rect.height


class Enemy(GameSprite):
    """敌机类"""

    def __init__(self):
        # 1.调用父类方法创建敌机精灵,同时指定敌机图片
        super().__init__("./images/enemy1.png")
        # 2.指定敌机的初始随机速度
        self.speed = random.randint(1, 3)
        # 3.指定敌机的初始随机位置
        self.rect.bottom = 0
        self.rect.x = random.randint(0, SCREEN_RECT.width - self.rect.width)

    def update(self, *args):
        # 1.调用父类方法,保持垂直方向的飞行
        super().update()
        # 2.判断是否飞出屏幕,如果是,需要从精灵组删除敌机
        if self.rect.y >= SCREEN_RECT.height:
            # kill方法可以自动将精灵从精灵组中移出,精灵就会被自动销毁
            self.kill()

    def __del__(self):
        print("敌机挂了 %s" % self.rect)


class Hero(GameSprite):
    """英雄精灵"""

    def __init__(self):
        # 1.调用父类方法设置image和speed
        super().__init__("./images/me1.png", 0)
        # 2.设置英雄的初始位置
        self.rect.centerx = SCREEN_RECT.centerx
        self.rect.bottom = SCREEN_RECT.bottom - 90
        self.bullets = pygame.sprite.Group()

    def update(self, *args):
        self.rect.x += self.speed

        if self.rect.x < 0:
            self.rect.x = 0
        elif self.rect.right > SCREEN_RECT.right:
            self.rect.right = SCREEN_RECT.right

    def fire(self):
        print("发射子弹~biu~biu~biu~")
        for i in (1, 2, 3):
            # 1.创建子弹精灵
            bullet = Bullet()
            # 2.设置精灵的位置
            bullet.rect.bottom = self.rect.y - i * 20
            bullet.rect.centerx = self.rect.centerx
            # 3.将子弹精灵添加到英雄的精灵组中
            self.bullets.add(bullet)


class Bullet(GameSprite):
    """子弹精灵"""

    def __init__(self):
        # 1.调用父类方法设置子弹图片
        super().__init__("./images/bullet1.png", -2)

    def update(self, *args):
        # 调用父类方法,让子弹沿垂直方向飞行
        super().update()

        # 判断子弹是否飞出屏幕
        if self.rect.bottom < 0:
            self.kill()

    def __del__(self):
        print("子弹被销毁")
