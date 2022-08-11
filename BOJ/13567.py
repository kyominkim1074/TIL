import sys
sys.stdin = open('13567.txt')
input = sys.stdin.readline
sys.setrecursionlimit(10000000)

dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]

n, m = map(int, input().split())
graph = [list(map(int, input().split())) for _ in range(n)]


def dfs(x, y):
    global cnt
    cnt += 1
    graph[x][y] = 0
    for i in range(4):
        nx = x+dx[i]
        ny = y+dy[i]
        if -1<nx<n and -1<ny<m and graph[nx][ny]==1:
            dfs(nx, ny)
            
list_ = []
for i in range(n):
    for j in range(m):
        if graph[i][j] == 1:
            cnt=0
            dfs(i, j)
            list_.append(cnt)
            
if len(list_)==0:
    print(len(list_))
    print(0)
else:
    print(len(list_))
    print(max(list_))