# n = int(input())
# mat = [input() for _ in range(n)]
# click = [input() for _ in range(n)]
# a = [['.' for _ in range(n)] for _ in range(n)]
# game = False

# dx = [-1, -1, -1, 0, 0, 1, 1, 1]
# dy = [-1, 0, 1, -1, 1, -1, 0, 1]

# for i in range(n):
#     for j in range(n):
#         if click[i][j] == 'x':
#             if mat[i][j] == "*":
#                 game = True
#             cnt = 0
#             for k in range(8):
#                 x = i + dx[k]
#                 y = j + dy[k]
#                 if 0 <= x < n and 0 <= y < n:
#                     if mat[x][y] == '*':
#                         cnt += 1
#             a[i][j] = str(cnt)
# if game:
#     for row in range(n):
#         for col in range(n):
#             if mat[row][col] == '*':
#                 a[row][col] = '*'
# for i in range(n):
#     print(''.join(a[i]))
    
#===============


#델타 탐색
delta_y = [-1, -1, -1, 0, 0, 1, 1, 1]
delta_x = [-1, 0, 1, -1, 1, -1, 0, 1]
mine = '*'
empty = '.'
n = 8
y, x = 1, 3
n = int(input())
game = [list(input()) for _ in range(n)]
open = [list(input()) for _ in range(n)]
mine_a = False

result = []
for i in range(n):
    temp = ['.'] * 8
    result.append(temp)

#2중
for y in range(n):
    for x in range(n):
        #현재 위치가 오픈한 위치
        # open => x
        if open[y][x] == 'x':
            mine_cnt = 0
            for d in range(8):
                search_y = y + delta_y[d]
                search_x = x + delta_x[d]
                #리스트의 범위 = 0 - 7
                if 0<=search_y<=n-1 and 0<=search_x<=n-1:
                    if game[search_y][search_x] == mine:
                        mine_cnt += 1
            result[y][x] = str(mine_cnt)
            
            # 현재 오픈한 위치에 지뢰가 있는지 확인
            if game[y][x] == mine:
                mine_a = True
# 지뢰를 발견했으면 모든 지뢰의 위치를 결과보드에 표시
if mine_a == True:
    for y in range(n):
        for x in range(n):
            if game[x][x] == mine:
                result[y][x] = mine

for row in result:
    print(''.join(row))