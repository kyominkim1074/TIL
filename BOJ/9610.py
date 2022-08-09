import sys
input = sys.stdin.readline

t = int(input())
q = [0]*5

for _ in range(t):
    x, y = map(int, input().split())
    if x == 0 or y == 0: #x 또는 y가 0이면 축에 점이 존재하기 때문에 axis
        q[0] += 1
    elif x > 0 and y > 0:
        q[1] += 1
    elif x > 0 and y < 0:
        q[4] += 1
    elif x < 0 and y > 0:
        q[2] += 1
    elif x < 0 and y < 0:
        q[3] += 1
        
print(f'Q1: {q[1]}\nQ2: {q[2]}\nQ3: {q[3]}\nQ4: {q[4]}\nAXIS: {q[0]}')