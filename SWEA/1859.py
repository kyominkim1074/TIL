import sys
input = sys.stdin.readline

t = int(input())
for case in range(1, t+1):
    day = int(input())
    m = list(map(int, input().split()))
    
    max_v = m[-1]
    result = 0
    
    for i in range(day-2, -1, -1):
        if m[i] >= max_v:
            max_v = m[i]
        else:
            result += max_v - m[i]

    print(f'#{case} {result}')