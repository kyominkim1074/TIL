import sys
input = sys.stdin.readline

a = input()
b = input()
i = 0
cnt = 0

#a의 길이에서 b의 길이를 뺀 길이의 이하일 때까지 반복
while i <= len(a) - len(b):
    #b의 길이만큼 자른 a의 값이 b와 같은 경우
    #cnt에 1 더해주고
    #i에 b의 길이만큼 더해준다.
    if a[i:i+len(b)] == b:
        cnt += 1
        i += len(b)
    #다른 경우에는 i에 1을 더해준다.
    else:
        i += 1
print(cnt)