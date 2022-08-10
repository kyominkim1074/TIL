import sys
input = sys.stdin.readline

s = input()

f_happy = s.count(':-)')
f_sad = s.count(':-(')

if f_happy < f_sad:
    print('sad')
elif f_happy > f_sad:
    print('happy')
elif f_happy == 0 and f_sad == 0:
    print('none')
elif f_happy == f_sad:
    print('unsure')