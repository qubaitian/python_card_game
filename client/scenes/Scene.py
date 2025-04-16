from __future__ import annotations
import os
import pygame
from pygame.event import Event
import pygame_gui
from config import config

pygame.init()

screen = pygame.display.set_mode((config.window_width, config.window_height))
manager = pygame_gui.UIManager(
    (config.window_width, config.window_height),
    theme_path="/Users/qubaitian/python_card_game/assets/theme.json",
)

console_window = pygame_gui.windows.UIConsoleWindow(
    rect=pygame.Rect(
        (config.window_width * 1 / 10, config.window_height * 1 / 10),
        (config.window_width * 8 / 10, config.window_height * 8 / 10),
    ),
    visible=False,
    manager=manager,
)

class Scene:
    next_scene: Scene = None

    def update(self, dt: float, events: list[Event]):
        """更新场景状态"""
        pass
