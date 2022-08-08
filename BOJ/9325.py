import sys
input = sys.stdin.readline

t = int(input())

for _ in range(t):
    s = int(input())
    n = int(input())
    re = s
    
    for _ in range(n):
        q, p = map(int, input().split())
        re += q*p
        
    print(re)