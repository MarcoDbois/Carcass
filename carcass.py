import pygame
import random
from enum import Enum



class Direction(Enum):
    NORTH = 0
    EAST = 1
    SOUTH = 2
    WEST = 3
    
class Dimension(Enum):
    WINDOW_WIDTH = 1060
    WINDOW_HEIGHT =980
    SQUARE_DIM=70
    MENU_WIDTH=80

class Params(Enum):
    PNG_DIR="png_tuiles/" 
    BACKGROUND="background_"+str(Dimension.WINDOW_HEIGHT.value)+".png"
    P_LATERAL="panneau_lateral_"+str(Dimension.WINDOW_HEIGHT.value)+".png"
    END_TUILE="fintoplace.png"
    CLICKABLE="greenSquare.png"
    
class Tuile(): 
    def __init__(self,ref,jpg,data):
        self.ref=ref
        self.jpg=jpg
        self.edges=data
   
    def calcul_edges(self,rotation):
        edgesCase=[]
        for i in range(4):
            edgesCase.append(self.edges[(i+rotation)%4])  
        return edgesCase


class Square() :
    def __init__(self,x,y,tuile,rot):
        
        self.position=(x,y)
        
        self.rot=rot
        self.tuile=tuile
        self.edges=self.tuile.calcul_edges(self.rot)
        
    def to_str(self):
        return str(self.position)+str(self.edges)
        
    
    def voisins(self):
        x,y=self.position
        voisins=[]
        for direction in range(4):
            if direction % 2 ==0:
                deltaX=0 
                if direction==0:
                    deltaY= -1
                else: deltaY=+1
            else: 
                deltaY=0
                if direction==1:
                    deltaX=1 
                else: deltaX=-1
            voisins.append((direction, (x+deltaX, y+deltaY)))
        return voisins  
 
        

class CarcassGame():
    
    def __init__(self):
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
        
        self.tourNum=1
        self.tour=True
        self.stack=random.sample(tuiles,len(tuiles))
        
        square0=Square(0,0,t0,0)        
        self.squares=[square0]
        self.clickablePlaces=[x[1] for x in square0.voisins()]
        
    def nextTuile(self):
        return self.stack[self.tourNum-1]
    
    def play(self,pos,rotation):
        newSquare=Square(pos[0],pos[1],self.nextTuile(),rotation)      
        voisins=[x for x in newSquare.voisins() if x[1] not in self.clickablePlaces]                      
        potentialNeighbours=[(sq,x[0]) for sq in self.squares for x in voisins if sq.position==x[1] ]
                        
        placable=True
        for p in potentialNeighbours:
            if p[0].edges[(p[1]+2)%4]!=newSquare.edges[p[1]]:
                placable=False                            
            else:
                voisins.remove((p[1],p[0].position))
                                
        if placable: 
            self.squares.append(newSquare)
            self.clickablePlaces.remove(newSquare.position)
            self.clickablePlaces.extend([voisin[1] for voisin in voisins])
            if self.tourNum<len(self.stack):
                self.tourNum+=1
            else:
                self.tourNum=0
                
        
        return placable
    
    

        
class Carcass():
      
    def __init__(self):
        
        pass
        
        pygame.init()
        self.gameDisplay = pygame.display.set_mode((Dimension.WINDOW_WIDTH.value, Dimension.WINDOW_HEIGHT.value))

#        Chargement et collage du fond
        fond = pygame.image.load(Params.PNG_DIR.value+Params.BACKGROUND.value).convert()
        self.gameDisplay.blit(fond, (Dimension.MENU_WIDTH.value,0))
        menu=pygame.image.load(Params.PNG_DIR.value+Params.P_LATERAL.value).convert()
        self.gameDisplay.blit(menu, (0,0))
        
        posTuileToPlace=((Dimension.MENU_WIDTH.value-Dimension.SQUARE_DIM.value)/2,(Dimension.WINDOW_HEIGHT.value-Dimension.SQUARE_DIM.value)/2)
        
        self.rectTuileToPlace=pygame.Rect(posTuileToPlace[0],posTuileToPlace[1],Dimension.SQUARE_DIM.value,Dimension.SQUARE_DIM.value)
        self.game=CarcassGame()
        
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
        self.gameDisplay.blit(tuile_img,rect)
        
    def displayTuileToPlace(self):
        self.displayTuile(self.game.nextTuile().jpg,self.rectTuileToPlace,self.rotTuileToplace) 
     

    #Renvoie un rect pygame de dimensions d'une case pour une case de position pos 
    def calculRectTuile(self,pos):
        x=pos[0]
        y=pos[1]
        
        xe= (Dimension.WINDOW_WIDTH.value+Dimension.MENU_WIDTH.value+(2*x-1)*Dimension.SQUARE_DIM.value)/2
        ye=(Dimension.WINDOW_HEIGHT.value+(2*y-1)*Dimension.SQUARE_DIM.value)/2
        
        rect=pygame.Rect(xe,ye,Dimension.SQUARE_DIM.value,Dimension.SQUARE_DIM.value)
        
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

carcass=Carcass()

while not carcass.crashed:
    carcass.update()
    
pygame.quit()
quit()
