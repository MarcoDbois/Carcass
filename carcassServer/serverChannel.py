
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
        pass
        #print(data["action"])
    
    def Network_play(self, data):
        print(data)
        self.PassOn(data)
        self._server.updateGameMove(data)
        

