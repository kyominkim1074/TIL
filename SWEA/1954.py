import sys
sys.stdin = open('1954.txt')
input = sys.stdin.readline

t = int(input())

dx = [0, 1, 0, -1]
dy = [1, 0, -1, 0]

for case in range(1, t+1):
    n = int(input())
    graph = [[0]*n for _ in range(n)]
    x=y=direc_=0
    cnt=1
    graph[x][y]=cnt
    cnt+=1
    
    while cnt<=n*n:
        nx=x+dx[direc_]
        ny=y+dy[direc_]
        
        if 0<=nx<n and 0<=ny<n and graph[nx][ny]==0:
            x=nx
            y=ny
            graph[x][y]=cnt
            cnt+=1
        else:
            direc_=(direc_+1)%4
    print(f'#{case}')
    for i in range(n):
        print(*graph[i])