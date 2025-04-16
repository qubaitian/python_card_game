import pygame
from scenes.Scene import Scene
from pygame.event import Event
from scenes.Scene import screen, console_window


class SelectCard(Scene):
    def __init__(self):
        # 初始化卡牌属性
        self.card_rect = pygame.Rect(300, 200, 150, 200)  # 卡牌位置和大小
        self.card_color = (200, 200, 200)  # 默认颜色
        self.is_hovered = False  # 鼠标悬停状态
        # 添加标题
        title_font = pygame.font.Font(None, 24)
        title_text = title_font.render("卡牌1", True, (255, 0, 0))
        title_rect = title_text.get_rect(center=self.card_rect.center)
        screen.blit(title_text, pygame.Rect(0, 0, 100, 100))

    def update(self, dt: float, events: list[Event]):
        if console_window.visible:
            return
        # 获取鼠标位置
        mouse_pos = pygame.mouse.get_pos()

        if not self.card_rect.collidepoint(mouse_pos):
            return

        # 检查鼠标是否在卡牌上
        if self.card_rect.collidepoint(mouse_pos):
            self.is_hovered = True
            self.card_color = (150, 150, 150)  # 悬停时变暗
        else:
            self.is_hovered = False
            self.card_color = (200, 200, 200)  # 恢复默认颜色

        # 填充背景
        screen.fill((0, 0, 0))
        # 绘制卡牌
        pygame.draw.rect(screen, self.card_color, self.card_rect)
        # 添加边框
        pygame.draw.rect(screen, (0, 0, 0), self.card_rect, 2)

        pygame.display.flip()
