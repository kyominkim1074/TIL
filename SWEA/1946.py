import sys
sys.stdin = open('1946.txt')
input = sys.stdin.readline

f = int(input())
for case in range (1, f+1):
    a = int(input())
    l = []
    for _ in range(a):
        al, n = map(str, input().split())
        for i in range(int(n)):
            l.append(al)
    print(f'#{case}')
    for i in range(len(l)):
        if i%10==9:
            print(l[i])
        else:
            print(l[i], end='')
    print()