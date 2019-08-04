from __future__ import print_function

import sys
from time import sleep, localtime
from random import randint,sample

from serverGame import Game


from PodSixNet.Server import Server
from PodSixNet.Channel import Channel



class ServerChannel(Channel):
    """
    This is the server representation of a single connected client.
    """
    
    def __init__(self, *args, **kwargs):
        Channel.__init__(self, *args, **kwargs)
        self.id = str(self._server.nextId())
        intid = int(self.id)
       
    
    def PassOn(self, data):
        # pass on what we received to all connected clients
        data.update({"id": self.id})
        
        self._server.SendToGamePlayers(data)
    """
    def Close(self):
        self._server.DelPlayer(self)
    """
    ##################################
    ### Network specific callbacks ###
    ##################################
    
    def Network(self, data):
        print(data["action"])
    
    def Network_play(self, data):
        print(data)
        self._server.updateGameData(data)
        self.PassOn(data)
"""
    def Network_drawpoint(self, data):
        self.lines[-1].append(data['point'])
        self.PassOn(data)
"""
class CarcassServer(Server):
    channelClass = ServerChannel
        
    def __init__(self, *args, **kwargs):
        self.id = 0
        Server.__init__(self, *args, **kwargs)
        self.games = []
        self.queue = None
        self.currentIndex=0
        self.players = []
        print('Server launched')
   
    def nextId(self):
        self.id += 1
        return self.id
  

    def Connected(self, channel,addr):
        #self.AddPlayer(channel)
        print('new connection:', channel, addr)
        channel.gameId= self.currentIndex if self.queue!=None else self.currentIndex+1
        channel.Send({"action": "setId", "id": channel.id,"gameId":channel.gameId})
        self.addPlayer(channel)
        
    def  addPlayer(self,channel): 
        if self.queue==None :
            self.currentIndex+=1
            self.queue=Game(self.currentIndex)
            self.queue.addPlayer(channel)
         
        else:
            print("hi")
            
            l=len(self.queue.players)
            
            if l<self.queue.nbPlayers-1:                
                self.queue.addPlayer(channel)
                print(self.queue.players)
                
            if l==self.queue.nbPlayers-1:
                self.queue.addPlayer(channel)
                players=[p.id for p in self.queue.players]
                print(players)
                
                for p in self.queue.players:
                    p.Send({"action": "initial", "init": self.queue.stack, "players": players, "gameId":self.queue.gameId})
                self.games.append(self.queue) 
                self.queue.printGame()
                self.queue=None   
            
            
            

    
    def launch(self):
        print("Started server on localhost ")  
        while True:
            self.Pump()
            sleep(0.0001)
    
    def SendToGamePlayers(self, data):
        senderId=data['id']
        gameId=data['gameId']
        [p.Send(data) for g in self.games for p in g.players if g.gameId==gameId and p.id!=senderId]
    
    def updateGameData(self,data):
        gameId=data['gameId']
        point=data['point']
        rotation=data['rotation']
        for g in self.games:
            if g.gameId==gameId:
                tuileId=g.stack[g.turn-1]
                g.playedSquares.append({"turnId":g.turn,"playerId":g.playerTurn().id,"tuile":tuileId,"point":point,"rotation":rotation})
                g.turn+=1
                g.printGame()
        pass
         
"""
    def AddPlayer(self, player):
        print("New Player" + str(player.addr))
        
        self.players[player] = True
        player.Send({"action": "initial", "init": stack, "players": [int(p.id) for p in self.players]})
        self.SendPlayers()
    def SendPlayers(self):
        self.SendToAll({"action": "players", "players": [int(p.id) for p in self.players]})
   
    def DelPlayer(self, player):
        print("Deleting Player" + str(player.addr))
        del self.players[player]
        self.SendPlayers()
    def SendToAll(self, data):
        [p.Send(data) for p in self.players]
"""       
    


# get command line argument of server, port
if __name__ == '__main__':
    if len(sys.argv) != 2:
        print("Usage:", sys.argv[0], "host:port")
        print("e.g.", sys.argv[0], "localhost:31425")
    else:
        host, port = sys.argv[1].split(":")
        s = CarcassServer(localaddr=(host, int(port)))
        s.launch()
        

