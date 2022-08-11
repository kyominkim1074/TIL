import sys
sys.stdin = open('25304.txt')
input = sys.stdin.readline

x = int(input())
n = int(input())

ab = 0
for _ in range(n):
    a, b = map(int, input().split())
    ab=ab+(a*b)
    
if x==ab:
    print('Yes')
else:
    print('No')