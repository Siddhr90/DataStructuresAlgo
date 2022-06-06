from collections import defaultdict

class Graph:
    def __init__(self, numberOfVertices):
        self.graph = defaultdict(list)
        self.numberOfVertices = numberOfVertices

    def addEdge(self, vertex, edge):
        self.graph[vertex].append(edge)

    def topologicalSortUtil(self, v, visited, stack):
        visited.append(v)                                   # O(1)

        for i in self.graph[v]:                             # O(E)
            if i not in visited:
                self.topologicalSortUtil(i, visited, stack)

        stack.insert(0, v)

    def topologicalSort(self):
        visited = []
        stack = []

        for k in list(self.graph):                      # goes through keys O(V+E)
            if k not in visited:
                self.topologicalSortUtil(k, visited, stack)     # O(E)

        print(stack)


customGraph = Graph(8)
customGraph.addEdge("A", "C")
customGraph.addEdge("C", "E")
customGraph.addEdge("E", "H")
customGraph.addEdge("E", "F")
customGraph.addEdge("F", "G")
customGraph.addEdge("B", "D")
customGraph.addEdge("B", "C")
customGraph.addEdge("D", "F")


customGraph.topologicalSort()
print(customGraph.graph)
print(list(customGraph.graph))