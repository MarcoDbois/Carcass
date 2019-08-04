from random import sample

class Game:
    def __init__(self, gameId,nbPlayers=3):
        # numéro du tour
        self.turn = 1
        # stack de la partie
        self.stack=sample([i for i in range(1,17)],16)
        #initialize the players including the one who started the game
        self.players=[]
        self.playedSquares=[]
        #gameId of game
        self.gameId=gameId  
        
        self.nbPlayers=nbPlayers 
    
    def addPlayer(self,player):
        self.players.append(player)
    
    def printGame(self):
        print("Game ",str(self.gameId),"\nplayers: ",[p.id for p in self.players],"\nstack: ",self.stack,'\n tuiles jouées :',self.playedSquares, "\nprochain tour: ",self.turn)
    
    def playerTurn(self):
        
        return self.players[self.turn%len(self.players)-1]
