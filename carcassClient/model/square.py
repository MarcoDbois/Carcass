from model.cardZone import CardZone

class Square() :
    def __init__(self,x,y,tuile,rot):
        
        self.position=(x,y)
        self.tuileRef=tuile.ref
        self.tuile=tuile
        self.rot=rot
        self.cardZones=tuile.calcul_cardZones(rot)
        self.graphCZ={}
        for z in self.cardZones:
            if z.type!="L":
                self.graphCZ[z]=[]
                if z.type=="R":
                    for l in self.cardZones:
                        if l.type=="L":
                            for x,y in z.edges:
                                for a,b in l.edges:
                                    if x==a and y==b:
                                        self.graphCZ[z].append(l)
                                        if l in self.graphCZ:
                                            self.graphCZ[l].append(z)
                                        else:
                                            self.graphCZ[l]=[z] 
                    
        self.edges=tuile.calcul_edges(self.rot)
        
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
            voisins.append((x+deltaX, y+deltaY))
        return voisins  
 
