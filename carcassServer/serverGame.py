from random import sample

class Game:
    def __init__(self, currentIndex,nbPlayers=3):
        # numéro du tour
        self.turn = 1
        # stack de la partie
        self.stack=sample([i for i in range(1,17)],16)
        #initialize the players including the one who started the game
        self.players=[]
        
        #gameId of game
        self.gameId=currentIndex  
        
        self.nbPlayers=nbPlayers 
    
    def addPlayer(self,player):
        self.players.append(player)
        
    def playerTurn(self):
        
        return self.turn%len(self.players)
