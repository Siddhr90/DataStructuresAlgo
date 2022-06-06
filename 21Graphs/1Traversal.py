class Graph:
    def __init__(self, gdict=None):
        if gdict is None:
            gdict = {}
        self.gdict = gdict

    def addEdge(self, vertex, edge):
        self.gdict[vertex].append(edge)

    def bfs(self,vertex):
        visited = [vertex]
        queue = [vertex]
        while queue:                        #  O(V)
            deQVertex = queue.pop(0)
            print(deQVertex)
            for adjacentVertex in self.gdict[deQVertex]:
                if adjacentVertex not in visited:               # O(E)
                    visited.append(adjacentVertex)
                    queue.append(adjacentVertex)

    def dfs(self, vertex):
        visited = [vertex]
        stack = [vertex]
        while stack:
            #print(visited)
            print(stack)
            destack = stack.pop()
            print(destack)
            for adjacentVertex in self.gdict[destack]:
                if adjacentVertex not in visited:
                    visited.append(adjacentVertex)
                    stack.append(adjacentVertex)




customDict = {"a" : ["b","c"],
            "b" : ["a","d","e"],
            "c" : ["a","e"],
            "d" : ["b","e","f"],
            "e" : ["d","f"],
            "f" : ["d","e"]
              }



graph = Graph(customDict)
graph.bfs("a")                      # time and space O(V+E)

customDict2 = {"a" : ["b","c"],
               "b" : ["a", "d", "g"],
               "c" : ["d","e","a"],
               "e" : ["c", "f"],
               "f" : ["e", "d", "g"],
               "d" : ["f", "c", "b"],
               "g" : ["b", "f"]
               }

graph2 = Graph(customDict2)
print("**********dfs*************")
graph2.dfs("a")                      # time and space O(V+E)