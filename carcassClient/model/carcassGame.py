from model.tuile import Tuile
from model.square import Square


t0=Tuile(0,"tuile0.png","PFFR")
                
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
t16=Tuile(16,"tuile16.png","RFFR")
tuiles=[t1,t2,t3,t4,t5,t6,t7,t8,t9,t10,t11,t12,t13,t14,t15,t16]


class CarcassGame():   
    def __init__(self,stack,players,playerId,gameId,nbPlayers=3):
        
        self.nbPlayers=nbPlayers
        self.playerId=playerId
        print(playerId)
        self.gameId=gameId
        print(gameId)
        self.players=players
        print(players)
        
        self.tourNum=1
        #self.tour=True if players.index(playerId)==0 else False
        self.tour=self.myTurn()
        self.stack=[t for o in stack for t in tuiles if t.ref==o] 
        
        square0=Square(0,0,t0,0)        
        self.squares=[square0]
        self.clickablePlaces=[x for x in square0.voisins()]
    
       
    def myTurn(self):
        return True if self.tourNum % self.nbPlayers==(self.players.index(self.playerId)+1) % self.nbPlayers else False        
    
        
    def tuileToPlace(self):
        return self.stack[self.tourNum-1]
    
    def play(self,pos,rotation):
        newSquare=Square(pos[0],pos[1],self.tuileToPlace(),rotation)      
        voisins=[(i,x) for i,x in enumerate(newSquare.voisins()) if x not in self.clickablePlaces]                      
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
            self.nextTurn()
        
        return placable
    
    def nextTurn(self):
        if self.tourNum<len(self.stack):
                self.tourNum+=1
                self.tour=self.myTurn()
                print(self.tour)
        else:
            self.tourNum=0
                
    
 
