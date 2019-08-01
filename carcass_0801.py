import pygame
import random
from model.tuile import Tuile
from model.carcassGame import CarcassGame
from params import Params
t0=Tuile(0,"tuile0.png","RFFR")
                
t1=Tuile(1,"tuile1.png","RRPR")
t2=Tuile(2,"tuile2.png","RFFF")
t3=Tuile(3,"tuile3.png","PPFP")
t4=Tuile(4,"tuile4.png","PPFF")
t5=Tuile(5,"tuile5.png","FPRP")
t6=Tuile(6,"tuile6.png","PRRP")
t7=Tuile(7,"tuile7.png","PFRP")
t8=Tuile(8,"tuile8.png","FFRF")
t9=Tuile(9,"tuile9.png","PPPP")
t10=Tuile(10,"tuile10.png","RPRR")
t11=Tuile(11,"tuile11.png","FPRR")
t12=Tuile(12,"tuile12.png","RRPR")
t13=Tuile(13,"tuile13.png","PFPF")
t14=Tuile(14,"tuile14.png","RPPR")
t15=Tuile(15,"tuile15.png","FRFR")
tuiles=[t1,t2,t3,t4,t5,t6,t7,t8,t9,t10,t11,t12,t13,t14,t15]
tuiles=random.sample(tuiles,len(tuiles))

pygame.init()
gameDisplay = pygame.display.set_mode((Params.WINDOW_WIDTH.value, Params.WINDOW_HEIGHT.value))

#        Chargement et collage du fond
fond = pygame.image.load(Params.PNG_DIR.value+Params.BACKGROUND.value).convert()
gameDisplay.blit(fond, (Params.MENU_WIDTH.value,0))
menu=pygame.image.load(Params.PNG_DIR.value+Params.P_LATERAL.value).convert()
gameDisplay.blit(menu, (0,0))
         
class Carcass():
      
    def __init__(self,tuiles=[]):
        
        pass
        
        posTuileToPlace=((Params.MENU_WIDTH.value-Params.SQUARE_DIM.value)/2,(Params.WINDOW_HEIGHT.value-Params.SQUARE_DIM.value)/2)
        
        self.rectTuileToPlace=pygame.Rect(posTuileToPlace[0],posTuileToPlace[1],Params.SQUARE_DIM.value,Params.SQUARE_DIM.value)
        
        self.game=CarcassGame(t0,tuiles)
        
        self.displayCarcassBoard()
        self.rotTuileToplace=0
        self.displayTuileToPlace()
        self.clock=pygame.time.Clock()
        self.crashed= False
        print(self.game.tourNum)

    def displayCarcassBoard(self):
        
        print(str(len(self.game.squares))+" squares")
        print([sq.to_str() for sq in self.game.squares])
        print(str(len(self.game.clickablePlaces))+" places")
        print([pos for pos in self.game.clickablePlaces])
        
        for square in self.game.squares:
            rect=self.calculRectTuile(square.position)
            self.displayTuile(square.tuile.jpg,rect,square.rot)
        
        for place in self.game.clickablePlaces:            
            rect=self.calculRectTuile(place)
            self.displayTuile(Params.CLICKABLE.value,rect,0)
            
            
                            
    def displayTuile(self,img,rect,rot):
        imgToPlace=pygame.image.load(Params.PNG_DIR.value+img).convert()   
        
        if rot==0:
            tuile_img=imgToPlace
        else: 
            tuile_img=pygame.transform.rotate(imgToPlace, rot*90)
        gameDisplay.blit(tuile_img,rect)
        
    def displayTuileToPlace(self):
        self.displayTuile(self.game.tuileToPlace().jpg,self.rectTuileToPlace,self.rotTuileToplace) 
     

    #Renvoie un rect pygame de dimensions d'une case pour une case de position pos 
    def calculRectTuile(self,pos):
        x=pos[0]
        y=pos[1]
        
        xe= (Params.WINDOW_WIDTH.value+Params.MENU_WIDTH.value+(2*x-1)*Params.SQUARE_DIM.value)/2
        ye=(Params.WINDOW_HEIGHT.value+(2*y-1)*Params.SQUARE_DIM.value)/2
        
        rect=pygame.Rect(xe,ye,Params.SQUARE_DIM.value,Params.SQUARE_DIM.value)
        
        return rect
    
    #determine si la position (x,y) appartient aux places cliquables 
    # retourne la position (x,y) si c'est le cas
    def inClickableRects(self,x,y):
    
        for pos in self.game.clickablePlaces:
            rect=self.calculRectTuile(pos)
            if rect.collidepoint(x,y):
                return pos
    

    def displayEndGame(self):
        
        self.displayTuile(Params.END_TUILE.value,self.rectTuileToPlace,0)
                                             
        print("GAME OVER")   
             
        
    def update(self):
        
        
        for event in pygame.event.get():       
            
            if event.type==pygame.QUIT:
                self.crashed=True
            if event.type== pygame.MOUSEBUTTONDOWN :
                    print(event)
            #
            if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1 and self.game.tourNum<=len(self.game.stack):
                
                if self.rectTuileToPlace.collidepoint(event.pos[0],event.pos[1]):
                    self.rotTuileToplace+=1
                    self.displayTuileToPlace()
                    
                else:
                
                    try: pos=self.inClickableRects(event.pos[0], event.pos[1])
                    except NameError: pos = None
                    print(pos)
                
                    if pos is not None:   
                        
                        placable=self.game.play((pos[0],pos[1]),self.rotTuileToplace)
                                
                        if placable: 
                            
                            self.rotTuileToplace=0  
                            self.displayCarcassBoard()  
                            
                            
                            if self.game.tourNum==0:
                                self.displayEndGame()
                                
                            else:
                                self.displayTuileToPlace()
                                 
                                print("\n")
                                
                        
                    
        pygame.display.flip()
        self.clock.tick(60)

carcass=Carcass(tuiles)

while not carcass.crashed:
    carcass.update()
    
pygame.quit()
quit()
