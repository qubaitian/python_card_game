import pygame
import sys

# 初始化Pygame
pygame.init()

# 设置屏幕尺寸
screen = pygame.display.set_mode((640, 480))
print(pygame.font.get_fonts())

# 设置背景颜色
background_color = (255, 255, 255)

# 创建字体对象
# font1 = pygame.font.SysFont('songti', 36)  # 使用系统字体
# font1 = pygame.font.Font('/Users/qubaitian/Downloads/庞门正道标题体.ttf', 24)  # 从文件加载字体
font1 = pygame.font.Font('/Users/qubaitian/genwan-font/ttc/GenWanMin2-M.ttc', 24)  # 从文件加载字体

# 渲染文本
text1 = font1.render('Hello, World!', True, (0, 0, 0))
text2 = font1.render('대기화면-종료화면', True, (255, 0, 0))
text3 = font1.render('一二三啊五一二三啊五然后在主题文件中为这个特定', True, (255, 0, 0))
text4 = font1.render('1234567890123456789012345678901234567890123456', True, (255, 0, 0))

# 主循环
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    # 填充背景
    screen.fill(background_color)

    # 绘制文本
    screen.blit(text1, (20, 20))
    screen.blit(text2, (20, 80))
    screen.blit(text3, (20, 140))
    screen.blit(text4, (20, 200))
    # 更新屏幕
    pygame.display.flip()

    # 控制帧率
    pygame.time.Clock().tick(60)
