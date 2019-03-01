import pygame
from game_snake.body import *
from game_snake.end import *
class Snake:
    def __init__(self,screen,diamonds,prop):
        self.x=190
        self.y=380
        self.head = pygame.image.load("picture/tou.gif").convert()
        self.screen = screen
        self.distance=[]
        self.diamonds=diamonds
        self.prop=prop
        self.gao=20
        self.leng=[]
        self.shenList=[]
        self.zuoBiao=[]
        self.end=End()
        self.score=0
    def display(self):
        self.screen.blit(self.head,(self.x, self.y))
        for i in self.leng:
            s=ShenTi(self.screen,self.x,self.y+i)
            s.display()
    def pProp(self):
        for b in self.prop.startList:
            for i in range(0,b[0]):
                ex=int(b[1][i])
                ey=int(b[3])
                if self.x+10 in range(ex,ex+20) and self.y in range(ey,ey+40):                   # print("吃到道具")
                    for a in range(0,b[2][i]):
                        self.addShen()
                    b[0]-=1
                    b[1].pop(i)
                    b[2].pop(i)

                    break
    def pDiamonds(self):
        for b in self.diamonds.squareList:
            for i in range(0,b[0]):
                ex=int((b[1][i]-1)*80)
                ey=int(b[3])
                if self.x+10 in range(ex,ex+80) and self.y in range(ey,ey+80):                   # print("碰到方块")
                    self.jianShen()
                    b[0]-=1
                    b[1].pop(i)
                    b[2].pop(i)
                    self.score+=1
                    break

    def left(self):
        self.x-=5
    def right(self):
        self.x+=5
    def up(self):
        self.y-= 5
    def down(self):
        self.y+=5
    def move(self,x,y):
        self.x=x-10
        self.y=y-10
    def addShen(self):

        self.leng.append(self.gao)
        self.gao+=20
    def jianShen(self):
        if len(self.leng)==0:
            print('游戏结束')
            self.end.setScore(self.score)
            self.end.main()
            pygame.quit()
        else:
            self.leng.pop()
            self.gao-=20