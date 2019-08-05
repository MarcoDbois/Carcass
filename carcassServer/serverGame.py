from random import sample

class Game:
    def __init__(self, gameId,nbPlayers=3):
        # numéro du tour
        self.turn = 1
        # stack de la partie
        self.stack=sample([i for i in range(1,17)],4)
        #initialize the players including the one who started the game
        self.players=[]
        self.playedSquares=[]
        #gameId of game
        self.gameId=gameId  
        
        self.nbPlayers=nbPlayers 
    
    def addPlayer(self,player):
        self.players.append(player)
    
    def nextTurn(self):
        self.turn+=1
    
    def printGame(self):
        print("Game ",str(self.gameId),"\nplayers: ",[p.id for p in self.players],"\nstack: ",self.stack,'\n tuiles jouées :',self.playedSquares)
       
        if self.turn<len(self.stack):
            print( "\nprochain tour: ",self.turn)
        else:
            print("game over")
            
    def playerTurn(self):
        
        return self.players[self.turn%len(self.players)-1]
