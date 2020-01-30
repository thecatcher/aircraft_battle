from aircraft_sprites import *


class AircraftBattle():
    """飞机大战主类"""

    def __init__(self):
        print("游戏初始化...")
        # 1.创建游戏窗口
        self.screen = pygame.display.set_mode(SCREEN_RECT.size)
        # 2.创建游戏时钟
        self.clock = pygame.time.Clock()
        # 3.调用私有方法,精灵和精灵组的创建
        self.__create_sprites()
        # 调用timer函数,订阅敌机出场事件
        pygame.time.set_timer(CREATE_ENEMY_EVENT, 1000)
        pygame.time.set_timer(HERO_FIRE_EVENT, 500)

    def __create_sprites(self):
        # 创建背景精灵
        # bg1 = Background("./images/background.png")
        # bg2 = Background("./images/background.png")
        # # 设置第二个背景初始位置在窗口正上方
        # bg2.rect.y = -bg2.rect.height

        bg1 = Background()
        bg2 = Background(True)
        # 创建背景精灵组
        self.bg_group = pygame.sprite.Group(bg1, bg2)
        # 创建敌机精灵组
        self.enemy_group = pygame.sprite.Group()

        # 创建英雄和英雄组
        self.hero = Hero()
        self.hero_group = pygame.sprite.Group(self.hero)

    def start_game(self):
        print("游戏开始...")

        while True:
            # 1.设置刷新帧率
            self.clock.tick(SCREEN_FPS)
            # 2.事件监听
            self.__event_handler()
            # 3.碰撞检测
            self.__check_collision()
            # 4.更新/绘制精灵组
            self.__update_sprites()
            # 5.更新显示
            pygame.display.update()

    def __event_handler(self):
        for each_event in pygame.event.get():
            # 判断是否退出游戏
            if each_event.type == pygame.QUIT:
                AircraftBattle.__game_over()
            elif each_event.type == CREATE_ENEMY_EVENT:
                print("敌机出场...")
                # 创建敌机精灵
                enemy = Enemy()
                # 将敌机精灵添加到精灵组
                self.enemy_group.add(enemy)
            # elif each_event.type == pygame.KEYDOWN and each_event.key == pygame.K_RIGHT:
            #     print("向右移动...")
            elif each_event.type == HERO_FIRE_EVENT:
                self.hero.fire()
        keys_pressed = pygame.key.get_pressed()
        if keys_pressed[pygame.K_RIGHT]:
            self.hero.speed = 2
        elif keys_pressed[pygame.K_LEFT]:
            self.hero.speed = -2
        else:
            self.hero.speed = 0

    def __check_collision(self):
        # 子弹摧毁敌机
        pygame.sprite.groupcollide(self.hero.bullets, self.enemy_group, True, True)

        # 敌机撞毁英雄
        enemys = pygame.sprite.spritecollide(self.hero, self.enemy_group, True)
        if len(enemys) > 0:
            self.hero.kill()
            AircraftBattle.__game_over()

    def __update_sprites(self):
        self.bg_group.update()
        self.bg_group.draw(self.screen)

        self.enemy_group.update()
        self.enemy_group.draw(self.screen)

        self.hero_group.update()
        self.hero_group.draw(self.screen)

        self.hero.bullets.update()
        self.hero.bullets.draw(self.screen)

    @staticmethod
    def __game_over():
        print("游戏结束...")
        pygame.quit()
        exit()


if __name__ == '__main__':
    game = AircraftBattle()
    game.start_game()
