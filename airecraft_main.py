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

    def __create_sprites(self):
        pass

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

    def __check_collision(self):
        pass

    def __update_sprites(self):
        pass

    @staticmethod
    def __game_over():
        print("游戏结束...")
        pygame.quit()
        exit()


if __name__ == '__main__':
    game = AircraftBattle()
    game.start_game()
