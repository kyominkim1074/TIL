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

#================================

dx=[-1, 0, 1, 0]
dy=[0, 1, 0, -1]

n, m = list(map(int, input().split()))

visited = [[False] * m for _ in range(n)]
graph = [list(map(int, input().split())) for _ in range(n)]
painting = 0
painting_list=[]
for sy in range(n):
    for sx in range(m):
        if not visited [sy][sx] and visited[sy][sx] == 1:
            #dfs
            stack = []
            stack.append([sy,sx])
            visited[sy][sx] = True
            
            painting += 1
            size = 0
            
            #스택이 비어있을 때까지
            while len(stack) != 0:
                y, x = stack.pop()
                
                size+=1
                
                #델타 탐색
                for d in range(4):
                    ny = y + dy[d]
                    nx = x + dx[d]
                    
                    #조건1 범위
                    if not (-1 < ny < n and -1 < nx < m):
                        continue
                    
                    #조건2 방문확인
                    if visited[ny][nx] == True:
                        continue
                    
                    #조건3 좌표값 = 1
                    if graph[ny][nx] != 1:
                        continue
                    #조건을 다 통과했을때
                    #stack에 다음 좌표를 넣고
                    #방문 처리
                    stack.append((ny,nx))
                    visited[ny][nx] = True
                    
            painting_list.append(size)
            
if len(painting_list) != 0:
    print(painting)
    print(max(painting_list))
else:
    print(0)
    print(0)