class Graph:
    def __init__(self, gdict=None):
        if gdict is None:
            gdict = {}
        self.gdict = gdict

    def bfs(self, start, end):
        queue = []
        queue.append([start])
        while queue:                                          # O(V) T-C
            #print(queue)
            path = queue.pop(0)
            #print('path',path)
            node = path[-1]                                   # last element
            if node == end:                                   # means we have reached destination, so we return path
                return path
            # otherwise we will visit all adjacent nodes
            for adjacent in self.gdict.get(node, []):         # O(E) T-C     # we use get to get adj, [] is default
                new_path = list(path)
                new_path.append(adjacent)
                queue.append(new_path)

customDict = { "a" : ["b", "c"],
                "b" : ["d", "g"],
                "c" : ["d", "e"],
                "d" : ["f"],
                "e" : ["f"],
                "g" : ["f"]
              }

g = Graph(customDict)
print(g.bfs("a", "f"))                              # O(E) since we are visiting only connected vertices
                                                    # as opposed to normal BFS in graphs. (E will be greater than V)
                                                    # This will work for un-weighted graphs only (not for weighted graphs)


