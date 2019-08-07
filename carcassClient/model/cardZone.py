class CardZone:
    def __init__(self,cardId,type,edges=[]):
        self.cardId=cardId
        self.type=type
        self.edges=edges
        
    def to_str(self):
        return str(self.cardId)+self.type+str(self.edges)
