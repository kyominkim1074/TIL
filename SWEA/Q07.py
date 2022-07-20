T = int(input())
for case in range(1, T+1):
    n = int(input())
    a = 0

    for i in range(1, n+1):
        if (i%2==0):
            a-=i
        else:
            a+=i
    print(f'#{case} {a}')