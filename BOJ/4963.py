import sys
sys.stdin = open('4963.txt')
sys.setrecursionlimit(10**6)
input = sys.stdin.readline


dx=[-1,1,0,0,-1,+1,-1,+1]
dy=[0,0,-1,1,-1,-1,+1,+1]

def dfs(x,y):
    for i in range(8):
        nx=x+dx[i]
        ny=y+dy[i]
        if 0<=nx<h and 0<=ny<w and map_[nx][ny] == 1:
            map_[nx][ny]=0
            dfs(nx,ny)

while True:
    w, h = map(int, input().split())
    if w==0 and h==0:
        break
    
    map_=[list(map(int, input().split())) for _ in range(h)]
    cnt=0
    for i in range(h):
        for j in range(w):
            if map_[i][j]==1:
                cnt+=1
                map_[i][j]=0
                dfs(i,j)
    print(cnt)