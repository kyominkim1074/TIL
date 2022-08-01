import sys
input = sys.stdin.readline

case = int(input())
dic = {}
for i in range(case):
    name = input().rstrip()
    if name not in dic:
        dic[name] = 1
    else:
        dic[name] += 1

for j in range(case-1):
    won = input().rstrip()
    dic[won] -= 1
    if(dic[won]==0):
        del dic[won]
print(*dic)