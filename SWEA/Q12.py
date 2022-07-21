#숫자가 아니라 str로
n = int(input())

for i in range(1, n+1):
    i = str(i)
    cnt = i.count('3') + i.count('6') + i.count('9')
    if cnt == 0:
        print(i, end=' ')
    else:
        print('-'*cnt, end=' ')
        
n = int(input())
a = ['3', '6', '9']
for i in range(1, n+1):
    cnt=0
    for j in str(i):
        if j in a:
            cnt += 1
    if cnt>0:
        i='-'*cnt
    print(i, end=' ')
    
n = int(input())
for i in range(1, n+1):
    cnt=0
    for j in str(i):
        if j%10==3 or  j%10==6 or j%10==9:
            cnt += 1
    if cnt>0:
        i='-'*cnt
    print(i, end=' ')