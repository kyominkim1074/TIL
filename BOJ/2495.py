import sys
sys.stdin = open('2495.txt')
input = sys.stdin.readline

for _ in range(3):
    n = input()
    a = 1
    cnt=1
    for i in range(1, len(n)):
        if n[i] == n[i-1]:
            cnt += 1
            if cnt > a:
                a=cnt
        else:
            cnt=1
            
    print(a)