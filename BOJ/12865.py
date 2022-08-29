import sys
sys.stdin = open('12865.txt')
input = sys.stdin.readline

n, k = map(int, input().split())

for _ in range(n):
    w, v = map(int, input().split())
    re = 0
    