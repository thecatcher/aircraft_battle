from aircraft_sprites import *

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

# 创建敌机
enemy1 = GameSprite("./images/enemy1.png")
enemy2 = GameSprite("./images/enemy1.png", 2)
enemy2.rect.x = 200

enemy_group = pygame.sprite.Group(enemy1, enemy2)

# 创建游戏时钟
clock = pygame.time.Clock()

# 定义rect记录飞机的初始位置
hero_rect = pygame.Rect(150, 300, 102, 126)

while True:
    clock.tick(60)

    # 修改飞机的位置
    hero_rect.y -= 1

    # 让英雄灰机从下面飞上来
    if hero_rect.bottom <= 0:
        hero_rect.y = 700

    # 重绘图像
    screen.blit(bg, (0, 0))
    screen.blit(hero, hero_rect)
    # 绘制敌机组//注意!先绘制背景,再搞其他的
    enemy_group.update()
    enemy_group.draw(screen)
    # 刷新图像
    pygame.display.update()
    # 获取事件
    #    event_list = pygame.event.get()
    #    if event_list:
    #        print(event_list)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()
