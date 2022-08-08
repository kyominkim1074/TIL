n, m = map(int, input().split())
board = [list(input()) for _ in range(n)]

board[0][0] = 1

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

v = [[0]*m for _ in range(n)]
q = [(0, 0)]
v[0][0] = 1

while q:
    x, y = q.pop(0)
    
    if x == n-1 and y == m-1:
        print(v[x][y])
        break
        
    for i in range(4):
        nx, ny = x + dx[i], y + dy[i]
        if 0 <= nx < n and 0 <= ny < m:
            if v[nx][ny] == 0 and board[nx][ny] == '1':
                v[nx][ny] = v[x][y] + 1
                q.append((nx, ny))