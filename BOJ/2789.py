#1
cam = list('CAMBRIDGE')
s = list(input())
for i in range(len(cam)):
    for j in range(len(s)):
        if cam[i] == s[j]:
            s[j] = ''
for i in s:
    print(i, end='')

#2

cam = list('CAMBRIDGE')
s = input()
for i in range(len(s)):
    if s[i] not in cam:
        print(s[i], end='')