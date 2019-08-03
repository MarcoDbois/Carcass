#from __future__ import print_function

import sys
from time import sleep
   
from PodSixNet.Connection import connection, ConnectionListener
from carcass import Carcass

class Client(ConnectionListener,Carcass):
    def __init__(self, host, port):
        
        self.players = []
        self.running=False
        
        Carcass.__init__(self)
        
        self.Connect((host, port))
        
    
    def Loop(self):
        self.Pump()
        connection.Pump()
        
        self.Events()
        #self.displayCarcassBoard()
    """  
        if "connecting" in self.statusLabel:
            self.statusLabel = "connecting" + "".join(["." for s in range(int(self.frame / 30) % 4)])
    """
    #######################    
    ### Event callbacks ###
    #######################
    #def PenDraw(self, e):
    #    connection.Send({"action": "draw", "point": e.pos})
    

    
    def play(self,pos):
        connection.Send({"action": "play", "point": pos,"rotation": self.rotTuileToplace,"gameId":self.gameId})
    
    ###############################
    ### Network event callbacks ###
    ###############################
    # reception de la stack du jeu
    def Network_initial(self, data):
        #self.initGame(data['t0']
        self.gameId=data["gameId"]
       
        print("ordre "+str(data['init']))
        #self.running=True
        self.initGame(data['init'],data["players"])
    # reception d'un coup des adversaires   
    def Network_play(self, data):
        self.game.play(data['point'],data['rotation'])
        print("tour ",self.game.tour)
        self.rotTuileToplace=0
        self.running=self.game.tour  
        self.displayCarcassBoard()
    
    def Network_setId(self,data):
        self.playerId=data['id']
        self.gameId=data['gameId']
    
    def Network_players(self, data):
        self.playersLabel = str(len(data['players'])) + " players"
        mark = []
        
        self.players=data['players']
        
    
    def Network(self, data):
        print('network:', data)
        pass
    
    def Network_connected(self, data):
        self.statusLabel = "connected"
    
    def Network_error(self, data):
        print(data)
        import traceback
        traceback.print_exc()
        self.statusLabel = data['error'][1]
        connection.Close()
    
    def Network_disconnected(self, data):
        self.crashed=True
        self.statusLabel += " - disconnected"

if __name__ == '__main__':
    if len(sys.argv) != 2:
        print("Usage:", sys.argv[0], "host:port")
        print("e.g.", sys.argv[0], "localhost:31425")
    else:
        host, port = sys.argv[1].split(":")
        c = Client(host, int(port))
        while not c.crashed:
            c.Loop()
            sleep(0.001)