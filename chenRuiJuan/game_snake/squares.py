import pygame,random
class Square:
    def __init__(self, screen):
        self.star1=pygame.image.load("picture/star1.gif").convert()
        self.star2 = pygame.image.load("picture/star2.gif").convert()
        self.star3 = pygame.image.load("picture/star3.gif").convert()
        self.star4 = pygame.image.load("picture/star4.gif").convert()
        self.star5 = pygame.image.load("picture/star5.gif").convert()
        self.screen = screen
        self.startList=[[2,[20,200],[2,5],100]]
        self.ser=[1,2,3,4,5]
        self.dic1={1:self.star1,2:self.star2,3:self.star3,4:self.star4,5:self.star5}
    def __crate_images(self):
        self.bomb_list.append (pygame.image.load("picture/enemy0_down4.png"))
    def creat(self):
        num=random.randint(0,2)
        startlist=random.sample(self.ser,num)
        locallist=random.sample(range(10,390,10),num)
        zu=[num,locallist,startlist,100]
        self.startList.append(zu)
    def display(self):
        for j in self.startList:
            if j[3]>600:
                self.startList.remove(j)
            else:
                if j[0]==0:
                    pass
                else:
                    for i in range(0,j[0]):
                        x=j[1][i]
                        key=j[2][i]
                        self.screen.blit(self.dic1[key], (x,j[3]))
    def remove(self):
        for i in self.startList:
            i[3]+=0.5

