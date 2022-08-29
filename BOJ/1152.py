import sys
sys.stdin = open('1152.txt')
input = sys.stdin.readline

a=list(map(str, input().split()))
cnt=0
for i in range(len(a)):
    cnt+=1
print(cnt)