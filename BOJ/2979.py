import sys
sys.stdin = open('2979.txt')
input = sys.stdin.readline

a, b, c = map(int, input().split())

table = [0]*100
answer = 0
for _ in range(3):
    start, end = map(int, input().split())
    for i in range(start-1, end-1):
        table[i] += 1
for j in table:
    if j == 1:
        answer += a*j
    if j == 2:
        answer += b*j
    if j == 3:
        answer += c*j
print(answer)