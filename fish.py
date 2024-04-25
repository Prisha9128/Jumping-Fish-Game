import pygame as pg

#here we don't need to initialise pg as it is already done in game.py
#inheriting Sprite class present in pygame.sprite module
class Fish(pg.sprite.Sprite): 
    def __init__(self,scale_factor):
        super(Fish,self).__init__() #super class k const call hogya
        self.image= pg.transform.scale_by(pg.image.load("assets/fish3.png").convert_alpha(),scale_factor)
#convert_alpha and not convert() for transparency of img
        self.rect = self.image.get_rect(center = (70,420)) 
        #center pt of fish

        self.y_velocity=0
        self.gravity=0
        self.flap_speed=250
        self.update_on=False


    def update(self,dt):
        if self.update_on:
            self.applyGravity(dt)

            if self.rect.y<=0 and self.flap_speed==250:
                self.rect.y=0
                self.flap_speed=0
                self.y_velocity=0
            elif self.rect.y>0 and self.flap_speed==0:
                self.flap_speed=250

    
    def applyGravity(self,dt):
        self.y_velocity+=self.gravity*dt
        self.rect.y+=self.y_velocity
        if self.rect.y > 350:
            self.rect.y = 350
    
    def flap(self,dt):
        self.y_velocity=-self.flap_speed*dt
        self.rect.y -= 160
    
   
    
    def resetPosition(self):
        self.rect.center=(70,420)
        self.y_velocity=0
    