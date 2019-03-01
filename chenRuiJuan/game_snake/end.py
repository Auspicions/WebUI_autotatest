import pygame,time,sys
class End:
    def __init__(self):
        pygame.init()
        self.screen = pygame.display.set_mode((400, 600))
        # 背景图
        self.background = pygame.image.load("picture/bground.jpg").convert()
        self.img = pygame.image.load("picture/得分.gif").convert()
        self.WHITE = (255, 255, 255)
        # 通过字体文件获得字体对象（字体，大小）
        self.fontObj = pygame.font.Font('resources/chinese.stsong.ttf', 50)
    def setScore(self,s):
        self.score=s
    def main(self):
        while True:
            self.screen.blit(self.background, (0, 0))
            self.screen.blit(self.img, (40, 120))
            # 配置要显示的文字
            textSurfaceObj = self.fontObj.render('' + str(self.score), True, self.WHITE)
            # 获得要显示的对象的rect
            textRectObj = textSurfaceObj.get_rect()
            textRectObj.center = (200, 203)
            self.screen.blit(textSurfaceObj, textRectObj)

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    print("关闭")
                    pygame.quit()
                    sys.exit()
            pygame.display.update()