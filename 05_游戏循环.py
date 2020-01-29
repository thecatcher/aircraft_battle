import pygame

pygame.init()

# 创建游戏窗口
screen = pygame.display.set_mode((480, 700))


# 加载背景图片
bg = pygame.image.load("./images/background.png")
# 将背景图片绘制到游戏窗口中
screen.blit(bg, (0, 0))
# 刷新游戏窗口
# pygame.display.update()


# 加载英雄小灰机

hero = pygame.image.load("./images/me1.png")
screen.blit(hero, (150, 300))
pygame.display.update()

# 创建游戏时钟

clock = pygame.time.Clock()

i=0
while True:
    clock.tick(1)
    print(i)
    i += 1
#    for event in pygame.event.get():
#        if event.type == pygame.QUIT:
#            pygame.quit()


pygame.quit()
