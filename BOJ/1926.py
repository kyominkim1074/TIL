import sys
from collections import deque
sys.stdin = open('1926.txt')
input = sys.stdin.readline

def bfs(x, y):
    size = 1
    queue = deque()
    queue.append((x,y))
    visited[x][y] = True
    
    while queue:
        x, y = queue.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            
            if (0 <= nx < n and 0 <= ny < m):
                if graph[nx][ny] == 1 and not visited[nx][ny]:
                    visited[nx][ny] = True
                    queue.append((nx,ny))
                    size+=1
    return size

n, m = map(int, input().split())
visited = [[False] * m for _ in range(n)]
graph = [list(map(int, input().split())) for _ in range(n)]

dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]

cnt=0
max_=0
for i in range(n):
    for j in range(m):
        if graph[i][j] == 1 and not visited[i][j]:
            cnt+=1
            max_=max(max_, bfs(i, j))
            
print(cnt)
print(max_)