import pygame

pygame.init()

hero_rect = pygame.Rect(100,500,120,126)

print("英雄的原点在: %d  %d"%(hero_rect.x,hero_rect.y))

print("英雄的大小是: %d %d"%(hero_rect.width,hero_rect.height))

pygame.quit()