import pygame as pg
from random import randint
class Stone:
    def __init__(self,self_factor1,move_speed):
        self.img_up=pg.transform.scale_by(pg.image.load("assets/stone.png").convert_alpha(),self_factor1)
        
        self.rect_up=self.img_up.get_rect()
        #self.stone_distance=300
        self.rect_up.y=320
        self.rect_up.x=900
        self.move_speed=move_speed
    
    def drawStones(self,win):
        win.blit(self.img_up,self.rect_up)
       
    
    def update(self,dt):
        self.rect_up.x-=int(self.move_speed*dt)
        
