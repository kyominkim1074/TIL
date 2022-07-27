t = int(input())
for case in range(t):
    a, ota = input().split()
    a = int(a)
    print(ota[:a-1], ota[a:], sep='')