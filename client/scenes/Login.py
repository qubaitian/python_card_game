import pygame
import pygame_gui
from scenes.Scene import Scene
from pygame.event import Event
from scenes.Scene import screen, manager
from config import config


class Login(Scene):

    def update(self, dt: float, events: list[Event]):
        for event in events:
            if (
                event.type == pygame_gui.UI_BUTTON_PRESSED
                and event.ui_element == self.hello_button
            ) or (event.type == pygame.KEYDOWN and event.key == pygame.K_RETURN):
                print(self.server_address_input.get_text())

            manager.process_events(event)

        # 更新UI 背景
        screen.fill((0, 0, 0))
        manager.update(dt)
        manager.draw_ui(screen)

