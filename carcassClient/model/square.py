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
            voisins.append((x+deltaX, y+deltaY))
        return voisins  
 
