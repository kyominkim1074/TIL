import sys
input = sys.stdin.readline

n, m = map(int, input().split())
visited = [0]*(n+1)#방문처리 리스트
graph = [[] for _ in range(n+1)] #인접리스트
cnt=0

def dfs(start):
    visited[start] = 1
    for a in graph[start]:
        if not visited[a]:
            dfs(a)

for _ in range(m):
    u, v = map(int, input().split())
    graph[u].append(v)
    graph[v].append(u)
    
for i in range(1, n+1):
    if not visited[i]:
        dfs(i)
        cnt+=1
print(cnt)