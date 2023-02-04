import pygame
class app():
    def __init__(self,w=600,h=600,target=None,bgcolor=(0,0,0),title="pygamegui"):
        self.w=w
        self.h=h
        self.target=target
        self.bgcolor=bgcolor
        self.title=title
        self.scren=pygame.display.set_mode((self.w,self.h))
        self.colock=pygame.time.Clock()
        self.eve=None
    def run(self):
        pygame.display.set_caption(self.title)
        while True:
            self.scren.fill(self.bgcolor)
            for eve in pygame.event.get():
                self.eve=eve
                if eve.type == pygame.QUIT:
                    exit()
            if self.target != None:
                self.target()
            pygame.display.update()
            self.colock.tick(60)
if __name__=="__main__":
    def test():
        print('gui')
    window=app(target=test)
    window.run()