from __future__ import print_function

import sys
from time import sleep, localtime
from random import randint,sample
from weakref import WeakKeyDictionary

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
        self.color = [(intid + 1) % 3 * 84, (intid + 2) % 3 * 84, (intid + 3) % 3 * 84] #tuple([randint(0, 127) for r in range(3)])
        self.lines = []
    
    def PassOn(self, data):
        # pass on what we received to all connected clients
        data.update({"id": self.id})
        self._server.SendToGamePlayer(data)
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
        self.players = WeakKeyDictionary()
        print('Server launched')
   
    def nextId(self):
        self.id += 1
        return self.id
  

    def Connected(self, channel,addr):
        #self.AddPlayer(channel)
        print('new connection:', channel, addr)
        if self.queue==None :
            self.currentIndex+=1
            channel.gameid=self.currentIndex
            
            self.queue=Game(self.currentIndex)
            self.queue.addPlayer(channel)
            
            
        else:
            l=len(self.queue.players)
            
            if l<self.queue.nbPlayers-1:                
                self.queue.addPlayer(channel)
                print(self.queue.players)
                
            if l==self.queue.nbPlayers-1:
                self.queue.addPlayer(channel)
                print(self.queue.players)
                for p in self.queue.players:
                    
                    index=self.queue.players.index(p)
                    
                    p.Send({"action": "initial", "init": self.queue.stack, "rank": index, "gameid":self.queue.gameid})
                self.games.append(self.queue) 
                self.queue=None   
            
            
            

    
    def launch(self):
        print("Started server on localhost ")  
        while True:
            self.Pump()
            sleep(0.0001)
 
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
        
    def SendToGamePlayer(self, data):
        senderId=data['id']
        gameId=data['gameid']
        [p.Send(data) for g in self.games for p in g.players if g.gameid==gameId and p.id!=senderId]

class Game:
    def __init__(self, currentIndex,nbPlayers=3):
        # numéro du tour
        self.turn = 1
        # stack de la partie
        self.stack=sample([i for i in range(1,16)],15)
        #initialize the players including the one who started the game
        self.players=[]
        
        #gameid of game
        self.gameid=currentIndex  
        
        self.nbPlayers=nbPlayers 
    
    def addPlayer(self,player):
        self.players.append(player)
        
    def playerTurn(self):
        
        return self.turn%len(self.players)
# get command line argument of server, port
if __name__ == '__main__':
    if len(sys.argv) != 2:
        print("Usage:", sys.argv[0], "host:port")
        print("e.g.", sys.argv[0], "localhost:31425")
    else:
        host, port = sys.argv[1].split(":")
        s = CarcassServer(localaddr=(host, int(port)))
        s.launch()
        

