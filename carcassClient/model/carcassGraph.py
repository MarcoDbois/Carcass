class CarcassGraph():
    def __init__(self,sq0):
        self.graph={}
        self.graph.update(sq0.graphCZ)
    def update(self,sq):
        self.graph.update(sq.graphCZ)
    def addEdge(self,v1,v2):
        self.graph[v1].append(v2)
        self.graph[v2].append(v1)
    def connexePart(self,node,mark=[],river=False):
        mark.append(node)
      
        for n in self.graph[node]:
            if n not in mark:
            
                if river and n.type=="L":
                    mark.append(n)
                 
                else:
                    self.connexePart(n,mark,river)
    
        return mark

    def allConnexe(self):
        connexions=[]
        conn=[]
        for n in self.graph:   
            if n not in conn:
                cx=connexePart(n,[])
                conn.extend(cx)
                connexions.append(cx)  
        return connexions  
    
    def zoneClosed(self,a):
        finished=True
        zad=None
        if a.type=="F":
            zone=self.connexePart(a,[])
          
            for w in zone:
                if len(self.graph[w])!=len(w.edges):
                    finished=False   
            print(finished) 
            if finished: 
                    zad=zone
                   
                
        if a.type=="R":
            zone=self.connexePart( a, [], True)
           
            riversOneEnding=[z for z in zone if z.type=="R" and len(z.edges)==1]
            if len(riversOneEnding)==2:
                zad=zone
               
        return zad
    
    def pointsZone(self,zone):
        points=0                
        if zone[0].type=="F":
            points=len(zone)*2
        elif zone[0].type=="R" or zone[0].type=="L":
            for w in zone:
                if w.type=="L":
                    points+=w.fishs
                else:
                    points+=1
        return points
            
    def printGraph(self):
        for k,v in self.graph.items():
            val=[va.to_str() for va in v]
            print(k.to_str(),val)
        print("\n")   
    

