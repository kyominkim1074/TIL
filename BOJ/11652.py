import sys
input=sys.stdin.readline
t = int(input())
dic_=dict()

for case in range(t):
    n = int(input())
    if n in dic_:
        dic_[n] += 1
    else:
        dic_[n] = 1

re = sorted(dic_.items(),key=lambda x:(-x[1], x[0]))
print(re[0][0])