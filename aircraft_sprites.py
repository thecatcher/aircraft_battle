import pygame

# 屏幕常量
SCREEN_RECT = pygame.Rect(0, 0, 480, 700)
# 刷新帧率
SCREEN_FPS = 60


class GameSprite(pygame.sprite.Sprite):

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
