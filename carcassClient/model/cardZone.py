class CardZone:
    
    def __init__(self, id, type, edges, fishs=0):
        
        self.zid=id
        self.type=type
        self.edges=edges
        self.fishs=fishs
        
    def to_str(self):
        return "zid: "+str(self.zid)+"  type "+self.type+"  cotés:"+str(self.edges)

