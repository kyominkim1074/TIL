import sys
input = sys.stdin.readline

#가로줄은 위에서 아래방향, 세로줄은 좌에서 우로 각각 19번까지
board = [list(map(int, input().split())) for _ in range(19)]
dx = [0, 1, 1, -1]
dy = [1, 0, 1, 1]


for x in range(19):
    for y in range(19):
        if board[x][y] != 0:
            dol = board[x][y]
#출력 두번째 줄에 다섯개의 바둑알 중에 가장 왼쪽에 있는 바둑알의 좌표이기 때문에
#출력시킬 바둑알을 기준으로 4방향으로 설정해야 한다.
#따라서 아래 for문을 4번 반복시켜야 한다.
            for i in range(4):
                cnt = 1
                nx = x + dx[i]
                ny = y + dy[i]
                #오목을 확인하기 위해 현재 좌표에서 각 방향으로 5칸씩 체크한다.
                while 0 <= nx <= 19 and 0 <= ny <= 19 and board[nx][ny] == dol:
                    cnt += 1
                    
                    if cnt == 5:
                        if 0 <= x - dx[i] < 19 and 0 <= y - dy[i] < 19 and board[x-dx[i]][y-dy[i]] == dol:
                            break
                        if 0 <= nx - dx[i] < 19 and 0 <= ny - dy[i] < 19 and board[nx-dx[i]][ny-dy[i]] == dol:
                            break
                        
                        print(dol)
                        print(x + 1, y + 1)
                        sys.exit(0)
                    
                    nx += dx[i]
                    ny += dy[i]
                    
print(0)