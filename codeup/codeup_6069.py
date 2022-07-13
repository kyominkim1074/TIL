# 평가 기준
# 점수 범위 : 평가
#  90 ~ 100 : A
#  70 ~   89 : B
#  40 ~   69 : C
#    0 ~   39 : D
# 로 평가되어야 한다.

# n=int(input())

# if n>=90:
#     print('A')
# else:
#     if n>=70:
#         print('B')
#     else:
#         if n>=40:
#             print('C')
#         else:
#             print('D')

# n=int(input())

# if n>=90:
#     print('A')
# elif n>=70:
#     print('B')
# elif n>=40:
#     print('C')
# else:
#     print('D')

# 평가 내용
# 평가 : 내용
# A : best!!!
# B : good!!
# C : run!
# D : slowly~
# 나머지 문자들 : what?

a=input()

if a == 'A':
    print('best!!!')
elif a == 'B':
    print('good!!')
elif a == 'C':
    print('run!')
elif a == 'D':
    print('slowly~')
else:
    print('what?')