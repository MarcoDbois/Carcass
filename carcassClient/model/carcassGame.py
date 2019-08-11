from model.tuile import Tuile
from model.square import Square
from model.cardZone import CardZone
from model.carcassGraph import CarcassGraph

t0=Tuile(0,"tuile0.png","PFFR",[{"type":"P","edges":[(3,3)]},
                                {"type":"P","edges":[(0,0),(3,1)]},
                                {"type":"F","edges":[(1,0),(2,0)]},
                                {"type":"R","edges":[(0,2)]},
                                {"type":"R","edges":[(3,2)]},
                                {"type":"L","edges":[(0,2),(3,2)],"fishs":1}]) 
        
t1=Tuile(1,"tuile1.png","RRPR",[{"type":"P","edges":[(0,3),(1,1)]},
                                {"type":"P","edges":[(0,1),(3,1)]},
                                {"type":"P","edges":[(1,3),(2,0),(3,3)]},
                                {"type":"R","edges":[(3,2)]},
                                {"type":"R","edges":[(0,2)]},
                                {"type":"R","edges":[(1,2)]},
                                {"type":"L","edges":[(0,2),(1,2),(3,2)],"fishs":1}
                                ])

t2=Tuile(2,"tuile2.png","RFFF",[{"type":"F","edges":[(1,0),(2,0)]},
                                {"type":"F","edges":[(3,0)]},
                                {"type":"P","edges":[(0,1)]},
                                {"type":"P","edges":[(0,3)]},
                                {"type":"R","edges":[(0,2)]}])


t3=Tuile(3,"tuile3.png","PPFP",[{"type":"F","edges":[(2,0)]},
                                {"type":"P","edges":[(0,0),(1,0),(3,0)]}])
t4=Tuile(4,"tuile4.png","PPFF",[{"type":"F","edges":[(2,0),(3,0)]}])

t5=Tuile(5,"tuile5.png","FPRP",[{"type":"P","edges":[(1,0),(2,3)]},
                                {"type":"P","edges":[(3,0),(2,1)]},
                                {"type":"F","edges":[(0,0)]},
                                {"type":"R","edges":[(2,2)]}])

t6=Tuile(6,"tuile6.png","PRRP",[{"type":"P","edges":[(3,3)]},{"type":"P","edges":[(0,0),(3,1)]},{"type":"F","edges":[(1,0),(2,0)]},{"type":"R","edges":[(3,2)]}])
t7=Tuile(7,"tuile7.png","PFRP",[{"type":"P","edges":[(3,3)]},{"type":"P","edges":[(0,0),(3,1)]},{"type":"F","edges":[(1,0),(2,0)]},{"type":"R","edges":[(3,2)]}])
t8=Tuile(8,"tuile8.png","FFRF",[{"type":"F","edges":[(0,0)]},{"type":"F","edges":[(1,0)]},{"type":"F","edges":[(3,0)]}])
t9=Tuile(9,"tuile9.png","PPPP",[{"type":"P","edges":[(3,3)]},{"type":"P","edges":[(0,0),(3,1)]},{"type":"F","edges":[(1,0),(2,0)]},{"type":"R","edges":[(3,2)]}])
t10=Tuile(10,"tuile10.png","RPRR")
t11=Tuile(11,"tuile11.png","FPRR")
t12=Tuile(12,"tuile12.png","RRPR")
t13=Tuile(13,"tuile13.png","PFPF",[{"type":"F","edges":[(1,0),(3,0)]}])
t14=Tuile(14,"tuile14.png","RPPR")
t15=Tuile(15,"tuile15.png","FRFR")
t16=Tuile(16,"tuile16.png","RFFR")
tuiles=[t1,t2,t3,t4,t5,t6,t7,t8,t9,t10,t11,t12,t13,t14,t15,t16]

    


class CarcassGame():   
    def __init__(self,stack,players,playerId,gameId,nbPlayers=3):
    #def __init__(self):   
        self.nbPlayers=nbPlayers
        self.playerId=playerId
        self.gameId=gameId        
        self.players=players      
        self.score={}
        for player in players:
            self.score[player]=0
        #self.score=0
        self.tourNum=1
        self.tour=True if players.index(playerId)==0 else False
        self.tour=self.myTurn()
        self.stack=[t for o in stack for t in tuiles if t.ref==o] 
        
        square0=Square(0,0,t0,0)        
        self.squares=[square0]

        self.clickablePlaces=square0.voisins()

        self.graph=CarcassGraph(square0)
        
        
    def tuileToPlace(self):
        return self.stack[self.tourNum-1]
    def playerTurn(self):
        return self.players[self.tourNum%len(self.players)-1]
    
    def tuileDep(self):
        return t0   
    def myTurn(self):
        return True if self.tourNum % self.nbPlayers==(self.players.index(self.playerId)+1) % self.nbPlayers else False        
    
    

    def nextTurn(self):
        self.tourNum+=1
        self.tour=self.myTurn()


    def play(self,pos,rotation):
        newSquare=Square(pos[0],pos[1],self.tuileToPlace(),rotation)      
        voisins=[(i,x) for i,x in enumerate(newSquare.voisins()) if x not in self.clickablePlaces]                      
        potentialNeighbours=[(sq,x[0]) for sq in self.squares for x in voisins if sq.position==x[1] ]
        zones=[]               
        placable=True
        for p in potentialNeighbours:
            if p[0].edges[(p[1]+2)%4]!=newSquare.edges[p[1]]:
                placable=False                            
            else:
                newSqZones=[(j,z) for z in newSquare.cardZones for i,j in z.edges if z.type!="L" and i==p[1]]
                neighbourZones=[(j,z) for z in p[0].cardZones for i,j in z.edges if z.type!="L" and i==(p[1]+2)%4]
        
                for i,wz in newSqZones:
                    for j,iz in neighbourZones:
                        if i==j:
                            zones.append((iz,wz))
        
            voisins.remove((p[1],p[0].position))
                                
        if placable: 
    
            self.graph.update(newSquare) 
                 
            for a,b in zones:
                self.graph.addEdge(a,b)
                zad=self.graph.zoneClosed(a)
                if zad is not None:
                    self.score[self.playerTurn()]+=self.graph.pointsZone(zad)

            print("score","joueur",self.playerTurn(),":",self.score[self.playerTurn()],"points")           
            self.squares.append(newSquare)
            self.clickablePlaces.remove(newSquare.position)
            self.clickablePlaces.extend([voisin[1] for voisin in voisins])  
            self.nextTurn()
            
        return placable
  
                
    
 
