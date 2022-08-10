import sys
input = sys.stdin.readline

sam = [int(input()) for _ in range(3)]
if sum(sam) == 180:
    if sam[0] == sam[1] == sam[2]:
        print('Equilateral')
    elif sam[0] == sam[1] or sam[0] == sam[2] or sam[1] == sam[2]:
        print('Isosceles')
    else:
        print('Scalene')
else:
    print('Error')