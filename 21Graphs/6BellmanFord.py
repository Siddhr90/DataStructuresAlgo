class Graph:
    def __init__(self, vertices):
        self.V = vertices                                           # number of vertices
        self.graph = []
        self.nodes = []

    def addEdge(self, s, d, w):                                     # source, destination, weight
        self.graph.append([s, d, w])

    def addNode(self, value):
        self.nodes.append(value)

    def printSolution(self, dist):
        print("Vertex distance from source")
        for key, value in dist.items():
            print(' ' + key, ': ', value)

    def bellmanFord(self, src):
        dist = {i : float("Inf") for i in self.nodes}       #O(V)              step1: set all distances to inf
        dist[src] = 0

        for _ in range(self.V-1):                           #O(V)              step2: run for v-1 iterations via graph
            for s, d, w in self.graph:                      #O(E)
                if dist[s] != float('Inf') and dist[s]+w < dist[d]:
                    dist[d] = dist[s] + w

        for s,d,w in self.graph:                            #O(E)               step3: identify negative cycle, run one more iteration
            if dist[s] != float("Inf") and dist[s] + w < dist[d]:
                print('Graph contains negative cycle')
                return

        self.printSolution(dist)

g = Graph(5)
g.addNode("A")
g.addNode("B")
g.addNode("C")
g.addNode("D")
g.addNode("E")
g.addEdge("A","C",6)
g.addEdge("A","D",6)
g.addEdge("B","A",3)
g.addEdge("C","D",1)
g.addEdge("D","C",2)
g.addEdge("D","B",1)
g.addEdge("E","B",4)
g.addEdge("E","D",2)


g.bellmanFord("E")                      # O(EV) time C, SpaceC ; O(V) (for creating dict)