import random
import pygame

# 屏幕常量
SCREEN_RECT = pygame.Rect(0, 0, 480, 700)
# 刷新帧率
SCREEN_FPS = 60
# 敌机出场事件
CREATE_ENEMY_EVENT = pygame.USEREVENT


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
        self.speed = random.randint(1,3)
        # 3.指定敌机的初始随机位置
        self.rect.bottom = 0
        self.rect.x = random.randint(0, SCREEN_RECT.width-self.rect.width)

    def update(self, *args):
        # 1.调用父类方法,保持垂直方向的飞行
        super().update()
        # 2.判断是否飞出屏幕,如果是,需要从精灵组删除敌机
        if self.rect.y >= SCREEN_RECT.height:
            # kill方法可以自动将精灵从精灵组中移出,精灵就会被自动销毁
            self.kill()
    def __del__(self):
        print("敌机挂了 %s"%self.rect)