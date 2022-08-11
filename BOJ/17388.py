import sys
input = sys.stdin.readline

s, k, h = map(int, input().split())

if s+k+h >= 100:
    print('OK')
elif s+k+h != 100:
    if min(s, k ,h) == s:
        print('Soongsil')
    elif min(s, k, h) == k:
        print('Korea')
    else:
        print('Hanyang')