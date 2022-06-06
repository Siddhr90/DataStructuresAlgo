class Graph:
    def __init__(self, gdict=None):
        if gdict is None:
            gdict = {}
        self.gdict = gdict

    def addEdge(self, vertex, edge):
        self.gdict[vertex].append(edge)

    def checkRoute(self, startNode, endNode):
        visited = [startNode]  #
        queue = [startNode]
        path = False  #

        while queue:
            #print("afterBreak")
            deVertex = queue.pop(0)  # queue.pop(0)
            for adjacentVertex in self.gdict[deVertex]:                     #
                if adjacentVertex not in visited:
                    if adjacentVertex == endNode:
                        path = True
                        #print("beforeBreak")
                        break
                    else:
                        visited.append(adjacentVertex)
                        queue.append(adjacentVertex)

        return path

customDict = { "a" : ["c", "d", "b"],
               "b" : ["j"],
               "c" : ["g"],
               "d" : [],
               "e" : ["f", "g"],
               "f" : ["i"],
               "g" : ["d", "h"],
               "h" : [],
               "i" : [],
               "j" : [],
               }

g = Graph(customDict)
print(g.checkRoute("a", "j"))