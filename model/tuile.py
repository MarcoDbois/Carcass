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
