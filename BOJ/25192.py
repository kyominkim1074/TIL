import sys
input = sys.stdin.readline

t = int(input())
chk_user={}
cnt = 0

for case in range(t):
    name = input()
    if name == 'ENTER':
        for key, value in chk_user.items():
            if value == 1:
                cnt += 1
        chk_user = {}
    else:
        if name not in chk_user:
            chk_user[name] = 1

for key,value in chk_user.items():
    if value == 1:
        cnt += 1
print(cnt)