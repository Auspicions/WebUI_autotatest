import pygame,time,sys
pygame.init()
screen=pygame.display.set_mode((400,600))

# 背景图
background=pygame.image.load("picture/index.png").convert()
screen.blit(background,(0,0))
start=pygame.image.load("picture/开始.gif").convert()
screen.blit(start,(70,380))

pygame.display.set_caption("蛇蛇碰方块")

# 加载背景音乐文件
pygame.mixer.music.load('music/bgmusic.mp3')
# 播放背景音乐，第一个参数为播放的次数（-1表示无限循环），第二个参数是设置播放的起点（单位为秒）
pygame.mixer.music.play(-1, 0.0)

while True:
    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            print('关闭')
            sys.exit()
        # 获得鼠标按下的位置
        if event.type == pygame.MOUSEBUTTONDOWN:  # 按下
            dianji=event.pos
            print("开始：",dianji)
            if dianji[0]>=69 and dianji[0]<=334 and dianji[1]>=380 and dianji[1]<=444:
                # 跳转到游戏界面
                from game_snake.game_page import *
    pygame.display.update()