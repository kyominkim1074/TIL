import sys
input = sys.stdin.readline

t = int(input())

for i in range(t):
    eng = list(input().split())

    for word in eng:
        print(word[::-1], end=' ')
    print()