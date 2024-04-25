import pygame as pg
import sys, time
from fish import Fish #importing predefined module
from stones import Stone
pg.init()

class Game:
    def __init__(self,move_speed):
        self.width = 700
        self.height = 530  #tuple is to be passed
        self.scale_factor = 0.05 #self.fish = Fish(self.scale_factor) 
        self.scale_factor1=0.3
        self.win =pg.display.set_mode((self.width, self.height))
        self.clock = pg.time.Clock()
        self.move_speed = move_speed
        self.start_monitoring=False
        self.score=0
        self.font=pg.font.Font("assets/font.ttf",24)
        self.score_text=self.font.render("Score: 0 ",True,(0,0,0))
        self.score_text_rect=self.score_text.get_rect(center=(100,30))

        self.restart_text=self.font.render("Restart: 0 ",True,(0,0,0))
        self.restart_text_rect=self.restart_text.get_rect(center=(300,450))
        self.fish=Fish(self.scale_factor)

        self.is_enter_pressed=False
        self.is_game_started=True
        self.stones=[]
        self.stones_generate_counter=150

        self.setUpBgAndGround()
        self.gameLoop()
         
        #pygame k and image module me load func ko call
#every  game has game loop to keep the game moving
#method call

    def gameLoop(self):
        #whenever last frame was created
        last_time = time.time()
        while True:
            #whenever new frame is created
            new_time = time.time()
            dt = new_time - last_time  #delta time calculation
            last_time = new_time

            for event in pg.event.get():
                if event.type == pg.QUIT:
                    pg.quit()
                    sys.exit()

                if event.type==pg.KEYDOWN and self.is_game_started:
                    if event.key==pg.K_RETURN:
                        self.is_enter_pressed=True
                        self.fish.update_on=True
                    if event.key==pg.K_SPACE and self.is_enter_pressed:
                        self.fish.gravity=10
                        self.fish.flap(dt)
                    #if event.key == pg.K_DOWN :
                        #self.fish.rect.y = 350
                 
                if event.type==pg.MOUSEBUTTONUP:
                    if self.restart_text_rect.collidepoint(pg.mouse.get_pos()):
                        self.restartGame()

            
            #self.clock.tick(60) #ensures game loop runs atmost 60fps
            self.updateEverything(dt)
            self.checkCollisions()
            self.checkScore()
            self.drawEverything()
            pg.display.update() 
            #iss frame m jo bhi changes hua h vo wind. m dikhega
            self.clock.tick(60)

    def restartGame(self):
        self.score=0
        self.score_text=self.font.render("Score: 0 ",True,(0,0,0))
        self.is_enter_pressed=False
        self.is_game_started=True
        self.fish.resetPosition()
        self.stones.clear()
        self.stones_generate_counter=150
        self.fish.update_on=False

    def checkScore(self):
       if len(self.stones)>0:
           if self.fish.rect.left>self.stones[0].rect_up.left and self.fish.rect.right<self.stones[0].rect_up.right and not self.start_monitoring:
              self.start_monitoring=True
           if self.fish.rect.left>self.stones[0].rect_up.right and self.start_monitoring:
              self.start_monitoring=False
              self.score+=1
              self.score_text=self.font.render(f"Score: {self.score}",True,(0,0,0))


    def checkCollisions(self):
        if len(self.stones):
            if self.fish.rect.bottom>530:
                self.fish.update_on=False
                self.is_enter_pressed=False
                self.is_game_started=False
            if (self.fish.rect.colliderect(self.stones[0].rect_up)):
                self.is_enter_pressed=False
                self.is_game_started=False

    def updateEverything(self,dt):
        if self.is_enter_pressed:
            self.water1_rect.x -= int(self.move_speed*dt)
            self.water2_rect.x -= int(self.move_speed*dt)
            self.water3_rect.x -= int(self.move_speed*dt)
    #if water 1 screen s bhr       
            if self.water1_rect.right < 0:
                self.water1_rect.x =  self.water3_rect.right

            if self.water2_rect.right < 0:
                self.water2_rect.x =  self.water1_rect.right

            if self.water3_rect.right < 0:
                self.water3_rect.x =  self.water2_rect.right

            if self.stones_generate_counter>150:
                self.stones.append(Stone(self.scale_factor1,self.move_speed))
                self.stones_generate_counter=0
                
            self.stones_generate_counter+=1

            #moving the stones
            for stone in self.stones:
                stone.update(dt)
            
            
            #removing stones if out of screen
            if len(self.stones)!=0:
                if self.stones[0].rect_up.right<0:
                    self.stones.pop(0)
                  
            #moving the bird
        self.fish.update(dt)

    def drawEverything(self):
        self.win.blit(self.bg_img,(0,-140)) #(0,0) top left corner
            #window me blit krna show krna
            #ye blit buffer m hua h is change ko dikhane k liye update krna hoga
        for stone in self.stones:
            stone.drawStones(self.win)
        self.win.blit(self.water_img1,self.water1_rect)
        self.win.blit(self.water_img2,self.water2_rect)
        self.win.blit(self.water_img3,self.water3_rect)
        self.win.blit(self.fish.image, self.fish.rect)
        self.win.blit(self.score_text,self.score_text_rect)
        if not self.is_game_started:
            self.win.blit(self.restart_text,self.restart_text_rect)


    def setUpBgAndGround(self):
         
        self.bg_img = pg.image.load("assets/desert.jpg").convert() 
        self.water_img1 = pg.image.load("assets/water.png").convert()
        self.water_img2 = pg.image.load("assets/water.png").convert()
        self.water_img3 = pg.image.load("assets/water.png").convert()
        
        self.water1_rect = self.water_img1.get_rect()
        self.water2_rect = self.water_img2.get_rect()
        self.water3_rect = self.water_img2.get_rect()

        self.water1_rect.x = 0
        self.water2_rect.x = self.water1_rect.right
        self.water3_rect.x = self.water2_rect.right
        self.water1_rect.y = 400
        self.water2_rect.y = 400
        self.water3_rect.y = 400

    
print("1.HARD")
print("2.EASY")
print("3.MEDIUM")
ch = int(input("INPUT 1, 2 OR 3: "))
if(ch == 1):
    game = Game(1000)
if(ch == 2):
    game = Game(400)
if(ch == 3):
    game = Game(700)

   


