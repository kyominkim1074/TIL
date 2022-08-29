import sys
sys.stdin = open('2460.txt')
input = sys.stdin.readline

re=0
n=0

for _ in range(10):
    in_, out_ = map(int, input().split())
    n -= in_
    n += out_
    re = max(re, n)
    
print(re)