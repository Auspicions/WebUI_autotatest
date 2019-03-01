import pygame,time,sys
from game_snake.snake import *
from game_snake.stars import *
from game_snake.squares import *
pygame.init()
screen=pygame.display.set_mode((400,600))
#背景图
background=pygame.image.load("picture/bground.jpg").convert()

WHITE = (255, 255, 255)
# 通过字体文件获得字体对象（字体，大小）
fontObj = pygame.font.Font('resources/chinese.stsong.ttf', 30)

pygame.display.set_caption("贪吃蛇碰方块")
star=Star(screen)
square=Square(screen)
snake=Snake(screen,star,square)
end=End()

num='4'
# 设置显示对象的坐标
a_num='0'

for i in range(0,3):
    snake.addShen()
while True:
    # 配置要显示的文字

    # end.main()
    # textSurfaceObj1=fontObj.render(''+a_num , True, WHITE)
    textSurfaceObj = fontObj.render('' + num, True, WHITE)
    # 获得要显示的对象的rect
    # textRectObj1 = textSurfaceObj1.get_rect()
    # textRectObj1.center = (150 , 50)
    textRectObj = textSurfaceObj.get_rect()
    textRectObj.center = (snake.x+10, snake.y - 20)
    screen.blit(background,(0, 0))
    # 绘制字体
    num = str(len(snake.leng))
    # a_num = str(end.setScore(snake.self.score))
    # screen.blit(textSurfaceObj1, textRectObj1)
    screen.blit(textSurfaceObj, textRectObj)
    snake.display()
    star.display()
    square.display()
    snake.pProp()
    snake.pDiamonds()
    for i in square.startList:
        if i[3]==300:
            bool=True
            break
        else:
            bool=False
    if bool:
        square.creat()
    square.remove()
    for j in star.squareList:
        if j[3]==200:
            bool=True
            break
        else:
            bool=False
    if bool:
        star.creat()
    star.move()
    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            print("关闭")
            pygame.quit()
            sys.exit()
        elif event.type==pygame.KEYDOWN:
            if event.key==pygame.K_SPACE:
                snake.addShen()
            else:
                pass
        elif event.type==pygame.MOUSEMOTION:
            snake.move(event.pos[0],event.pos[1])
            y=event.pos[1]

    pygame.display.update()

