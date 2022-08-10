import sys
input = sys.stdin.readline

n = int(input())
m = int(input())

graph = [[0]*(n+1) for _ in range(n+1)]
for _ in range(m):
    a, b = map(int, input().split())
    graph[a][b]=1
    graph[b][a]=1

def bfs(gam):
    queue = [gam]
    f=[gam]
    while queue:
        current_=queue.pop()
        for serching in range(len(graph[current_])):
            if graph[current_][serching] and serching not in f:
                f += [serching]
                queue += [serching]
    return len(f)-1

print(bfs(1))

n=int(input()) #정점개수
m=int(input()) #간선개수
graph=[[] for _ in range(n+1)] #인접리스트
visited = [0]*(n+1)
total = 0

def dfs(start):
    stack = [start]
    visited[start] = 1
    
    while stack:
        cur = stack.pop()
        
        for adj in graph[cur]:
            if not visited[adj]:
                visited[adj] = 1
                stack.append(adj)