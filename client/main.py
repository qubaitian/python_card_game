# Example file showing a circle moving on screen
import pygame
import pygame_gui
from scenes.SelectCard import SelectCard
from scenes.Login import Login
from scenes.Scene import manager, screen, console_window
from config import config


# pygame setup
clock = pygame.time.Clock()
running = True
dt = 0

current_scene = SelectCard()

while running:
    events = pygame.event.get()
    for event in events:
        if event.type == pygame.QUIT:
            running = False

        if event.type == pygame_gui.UI_WINDOW_CLOSE:
            if event.ui_element == console_window:
                console_window = pygame_gui.windows.UIConsoleWindow(
                    rect=pygame.Rect(
                        (config.window_width * 1 / 10, config.window_height * 1 / 10),
                        (config.window_width * 8 / 10, config.window_height * 8 / 10),
                    ),
                    window_title="Console",
                    visible=0,
                    manager=manager,
                ) 
        
        # 按 ` 唤出 console
        if event.type == pygame.KEYDOWN and (event.scancode == 53 or event.key == pygame.K_BACKQUOTE):
            if console_window.visible:
                console_window.hide()
            else:
                console_window.show()

        if event.type == pygame_gui.UI_CONSOLE_COMMAND_ENTERED:
            if event.ui_element == console_window:
                # print the command in cosole
                print(event.command)
                console_window.add_output_line_to_log("这是一个测试输出", is_bold=True)

        manager.process_events(event)

    # 更新场景
    current_scene.update(dt, events)

    # # 检查是否需要切换场景
    # if current_scene.next_scene:
    #     current_scene = current_scene.next_scene
  
    manager.update(dt)
    manager.draw_ui(screen)

    pygame.display.flip()
    dt = clock.tick(60) / 1000

pygame.quit()
