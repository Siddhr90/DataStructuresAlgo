# Floyd Warshall

# here we declare inf for infinity and set it to 999
INF = 999

def printSolution(nV, distance):
    for i in range(nV):
        for j in range(nV):
            if(distance[i][j] == INF):
                print("INF", end=" ")
            else:
                print(distance[i][j], end="  ")
        print(" ")

def floydWarshall(nV, G):
    distance = G
    for k in range(nV):                         # to take all vertices one by one as source vertex
        for i in range(nV):                     # to visit each cell in the array (i for row and j for column)
            for j in range(nV):
                distance[i][j] = min(distance[i][j], distance[i][k]+distance[k][j])

    printSolution(nV, distance)

# we will create graph using 'adjacency matrix'

G = [[0, 8, INF, 1],
     [INF, 0, 1, INF],
     [4, INF, 0, INF],
     [INF, 2, 9, 1]
    ]

floydWarshall(4,G)                  # O(V^3) time C, O(V^2) space c(to create the FW matrix)
