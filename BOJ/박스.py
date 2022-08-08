import sys
input = sys.stdin.readline

# t = int(input())

# for _ in range(t):
#     m, n = map(int, input().split())
#     grid = [[] for _ in range(n)]
#     for i in range(m):
#         mat = list(input().split())
#         for g in range(n):
#             grid[g].append(mat[g])
    
#     cnt = 0
    
#     for i in range(n):
#         n = mat[i].count('1')
#         f = m - 1
        
#         for j in range(m-1, -1, -1):
#             if grid[i][j] == '1':
#                 cnt += f-j
#                 f -= 1
    
#     print(cnt)
    
    
    #=========================
    

box=1
empty=0
    
row, col = 5, 4

box_list = [[1, 0, 0 ,0],
            [0, 0, 1, 0],
            [1, 0, 0, 1],
            [0, 1, 0, 0],
            [1, 0, 1, 0]]
moving = 0


for x in range(col):
    for y in range(row-1, -1, -1): # = reversed(range()), list(range())[::-1]
        if box_list[y][x] == box:
            
            #조건문에서 범위에서 벗어나지 않게 순서에 맞게 작성
            if y+1 != row and box_list[y+1][x] != box:
                box_list[y][x] = empty
                box_list[y+1][x] = box
                y += 1
                moving += 1
            #while문
            while True:
                if y+1 == row:
                    break
                
                if box_list[y+1][x] == box:
                    break
                
                box_list[y][x] = empty
                box_list[y+1][x] = box
                y += 1
                moving += 1
print(moving)