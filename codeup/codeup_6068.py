# 평가 기준
# 점수 범위 : 평가
#  90 ~ 100 : A
#  70 ~   89 : B
#  40 ~   69 : C
#    0 ~   39 : D
# 로 평가되어야 한다.

n=int(input())

if n>=90:
    print('A')
else:
    if n>=70:
        print('B')
    else:
        if n>=40:
            print('C')
        else:
            print('D')

n=int(input())

if n>=90:
    print('A')
elif n>=70:
    print('B')
elif n>=40:
    print('C')
else:
    print('D')