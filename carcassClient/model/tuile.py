from model.cardZone import CardZone

class Tuile(): 
    def __init__(self,ref,jpg,edges,cardZones=[]):
        self.ref=ref
        self.jpg=jpg
        self.edges=edges
        self.czones=cardZones
        
    def calcul_edges(self,rotation):
        edgesCase=[]
        for i in range(4):
            edgesCase.append(self.edges[(i+rotation)%4])  
        return edgesCase
    
    #[[(1,0),(2,0)]]
    def calcul_cardZones(self,rotation):
        zones=[]
        for cz in self.czones:
            if "fishs" in cz:
                fishs=cz["fishs"]
            else:
                fishs=0
            d=CardZone(self.ref,cz["type"],[self.rotationCardZone(x,y,rotation) for x,y in cz["edges"]],fishs)
            
            zones.append(d)
        
        return zones
   
    def rotationCardZone(self,x,y,rotation):   
        xd, yd=x, y
        if yd%2!=0:
            for i in range(rotation):
                yd =(yd+2)%4 if xd%2==0 else yd     
                xd=(xd-1)%4
        return ((x-rotation)%4,yd)          
    
            