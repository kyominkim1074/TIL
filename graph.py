edges = [
    [0,1],
    [0,2],
    [1,3],
    [1,4],
    [2,4],
    [2,5],
    [4,6]
]

n=7

matrix = [[0]*n for _ in range(n)]

for edge in edges:
    v1, v2 = edge[0], edge[1]
    matrix[v1][v2] = 1
    matrix[v2][v1] = 1
    
n = 7
m=7

graph = [[] for _ in range(n)]

for _ in range(m):
    v1, v2 = map(int, input().split())
    graph[v1].append(v2)
    graph[v2].append(v1)