import sys
input = sys.stdin.readline

n = int(input()) # 전체 사람의 수
#촌수를 계산해야 하는 서로다른 두 사람의 번호
a, b = map(int, input().split())
#부모자식 간의 관계의 수
m=int(input())
graph=[[] for _ in range(n+1)]
visited=[0]*(n+1) # 방문 유무
re=[0]*(n+1) # 촌수
for _ in range(m):
    x, y = map(int, input().split())
    graph[x].append(y)
    graph[y].append(x)

def dfs(v):
    visited[v] = 1
    for i in graph[v]:
        if not visited[i]: # 방문하지 않은 경우 촌수+1
            re[i] = re[v]+1
            dfs(i)

dfs(a) # a번 정점에서 시작

if re[b]>0:
    print(re[b])
else:
    print('-1')