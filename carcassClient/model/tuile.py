class Tuile(): 
    def __init__(self,ref,jpg,edges,woods=[]):
        self.ref=ref
        self.jpg=jpg
        self.edges=edges
        self.czones=woods
   
    def calcul_edges(self,rotation):
        edgesCase=[]
        for i in range(4):
            edgesCase.append(self.edges[(i+rotation)%4])  
        return edgesCase
    
    #[[(1,0),(2,0)]]
    def calcul_cardZones(self,rotation):
        zones=[[(x-rotation)%4 for x in cz] for cz in self.czones]
        #for cz in self.czones:
        #    zlist=[]
        #    for x in cz:
        #        zlist.append((x-rotation)%4)
        #    zones.append(zlist)
        return zones
    
                   
            
            