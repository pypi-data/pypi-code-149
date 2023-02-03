import pygame

class button():
    def __init__(self,w=50,h=50,color=(0,0,255),color1=(0,255,0),target=None,text=None,fg="white"):
        self.h=h
        self.w=w
        self.color=color
        self.color1=color1
        self.target=target
        self.text=text
        self.fg=fg
        pygame.font.init()
        self.font = pygame.font.Font("font/AGENCYR.TTF", self.h-3)
    def show_no_anemi(self,x,y,window,boder_width=0,corner_round_level=0):
        
        #--------for target-----------
        mouse=pygame.mouse.get_pos()
        rect=pygame.Rect(x,y,self.w,self.h)
        if self.target!=None:
            if rect.collidepoint(mouse):
                if window.eve.type == pygame.MOUSEBUTTONDOWN:
                    self.target()
        #------------------------------

        #---------draw rect-----------------
        pygame.draw.rect(window.scren,self.color,rect,boder_width,corner_round_level)
        #------------------------------------
        
        #-------for text----------------
        if self.text!=None:
            txt=self.font.render(self.text,True,self.fg)
            window.scren.blit(txt,(x,y-8))
        #--------------------------------
        
    def show_color_change(self,x,y,window,boder_width=0,corner_round_level=0):
        #-------------some variables------------
        color=self.color
        mouse=pygame.mouse.get_pos()
        rect=pygame.Rect(x,y,self.w,self.h)
        #----------------------------------------
        
        #---------far target---------------------
        if self.target!=None:
            if rect.collidepoint(mouse):
                if window.eve.type == pygame.MOUSEBUTTONDOWN:
                    self.target()
                    color=self.color1
        #---------------------------------------

        #-------draw rect-------------
        pygame.draw.rect(window.scren,color,rect,boder_width,corner_round_level)
        #------------------------------

        #-------for text----------------
        if self.text!=None:
            txt=self.font.render(self.text,True,self.fg)
            window.scren.blit(txt,(x,y-8))
        #--------------------------------