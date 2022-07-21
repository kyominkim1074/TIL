#1
#숫자로 접근하지 말기
T = int(input())
for tc in range(1, T+1):
    n=int(input())
    #set에 중복을 제외하고 계속 추가
    s=set()
    cnt=1
    while True:
        for num in list(str(n)):
            s.add(num)
        if len(s) == 10:
            break
        n//=cnt
        cnt+=1
        n*=cnt
    print('#{} {}'.format(tc, n))

#2
T = int(input())
for tc in range(1, T+1):
    n=int(input())
    n1 = n
    #set에 중복을 제외하고 계속 추가
    s=set()
    cnt=1
    while True:
        for num in list(str(n)):
            s.add(num)
        if len(s) == 10:
            break
        n+=n1
    print('#{} {}'.format(tc, n))