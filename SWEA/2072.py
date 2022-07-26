T = int(input())
for test_case in range(1, T + 1):
    a = list(map(int, input().split()))
    re = 0
    for i in a:
        if i%2!=0:
            re+=i
    print(f'#{test_case} {re}')