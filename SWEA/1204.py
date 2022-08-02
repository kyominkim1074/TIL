import sys

sys.stdin = open("input1204.txt")

t = int(input())
for tc in range(1, t+1):
    num = int(input())
    a = {}
    n = map(int, input().split())
    
    for i in n:
        if i not in a:
            a[i] = 1
        else:
            a[i] += 1
        
    result = sorted(a.keys(), reverse=True)
    print(f'#{tc} {max(result, key=a.get)}')