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
