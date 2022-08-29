import sys
sys.stdin = open('10807.txt')
input = sys.stdin.readline

n = int(input())
num = list(map(int, input().split()))
v=int(input())
cnt=num.count(v)
print(cnt)