#왼쪽

matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]]

n = 3
rotated_matrix = [[0] * n for _ in range(n)]

for i in range(n):
    for j in range(n):
        rotated_matrix[i][j] = matrix[j][n-i-1]
        
#오른쪽

matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]]

n = 3
rotated_matrix = [[0] * n for _ in range(n)]

for i in range(n):
    for j in range(n):
        rotated_matrix[i][j] = matrix[n-j-1][i]
