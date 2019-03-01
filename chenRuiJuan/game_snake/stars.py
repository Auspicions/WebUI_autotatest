import pygame, random
class Star:
    def __init__(self,screen):
        self.square1=pygame.image.load("picture/square1.gif").convert()
        self.square2 = pygame.image.load("picture/square2.gif").convert()
        self.square3 = pygame.image.load("picture/square3.gif").convert()
        self.square4 = pygame.image.load("picture/square4.gif").convert()
        self.square5 = pygame.image.load("picture/square5.gif").convert()
        self.square6 = pygame.image.load("picture/square6.gif").convert()
        self.square7 = pygame.image.load("picture/square7.gif").convert()
        self.square8 = pygame.image.load("picture/square8.gif").convert()
        self.square9 = pygame.image.load("picture/square9.gif").convert()
        self.screen = screen
        self.local=[1,2,3,4,5]
        self.color=[1,2,3,4,5,6,7,8,9]
        self.squareList=[[3,[1,3,5],[2,4,6],0]]
        self.dic1={1:self.square1,2:self.square2,3:self.square3,4:self.square4,5:self.square5,6:self.square6,7:self.square7,8:self.square8,9:self.square9}
    def creat(self):
        zu=[]
        num=random.randint(1,5)
        randomlist= random.sample(self.local,num)
        squarelist=random.sample(self.color,num)
        zu.append(num)
        zu.append(randomlist)
        zu.append(squarelist)
        zu.append(0)
        self.squareList.append(zu)
    def display(self):
        for j in self.squareList:
            if j[3] > 600:
                self.squareList.remove(j)
            else:
                for i in range(0,j[0]):
                    x=(j[1][i]-1)*80
                    key=j[2][i]
                    self.screen.blit(self.dic1[key], (x,j[3]))

    def move(self):
        for i in self.squareList:
            i[3]+=0.5
