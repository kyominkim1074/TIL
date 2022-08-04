import sys
input = sys.stdin.readline

t = int(input())
for i in range(t):
    number = list(map(int, input().split()))
    number.sort()
    print(number[-3])