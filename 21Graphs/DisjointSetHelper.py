# disjoint set

class DisjointSet:
    def __init__(self, vertices):                               # O(N) time and space C
        self.vertices = vertices
        self.parent = {}
        for v in vertices:                                      # we are initializing the parent of the vertices to itself
            self.parent[v] = v
        self.rank = dict.fromkeys(vertices, 0)

    def find(self, item):                                       # O(1) time and space C, prints the parent
        if self.parent[item] == item:                           # if the parent is the current element
            return item
        else:
            return self.find(self.parent[item])

    def union(self, x, y):                                      # O(1) time and space C
        xroot = self.find(x)
        yroot = self.find(y)
        if self.rank[xroot] < self.rank[yroot]:
            self.parent[xroot] = yroot
        elif self.rank[xroot] > self.rank[yroot]:
            self.parent[yroot] = xroot
        else:
            self.parent[yroot] = xroot
            self.rank[xroot] += 1

vertices = ["A", "B", "C", "D", "E"]

ds = DisjointSet(vertices)
print(ds.find("A"))
ds.union("A","B")                       # sets first set as the parent of next set
print(ds.find("B"))
ds.union("A", "C")
print(ds.find("C"))


