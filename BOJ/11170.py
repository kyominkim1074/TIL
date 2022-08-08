import sys
input = sys.stdin.readline

t = int(input())
for _ in range(t):
    cnt = 0
    n, m = map(int, input().split())
    
    for i in range(n, m+1):
        zero_ = str(i)
        cnt += zero_.count('0')
    print(cnt)