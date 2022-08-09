import sys
input = sys.stdin.readline

#행, 열
r, c = map(int, input().split())
a = [0]*5

parking = []
for _ in range(r):
    parking.append(input())

for i in range(r):
    for j in range(c):
        if i+1 == r or j+1 == c:
            break
        #자동차가 차지하는 크기
        x1 = parking[i][j]
        x2 = parking[i][j+1]
        x3 = parking[i+1][j]
        x4 = parking[i+1][j+1]
        
        hap = x1+x2+x3+x4
        
        if '#' in hap:
            continue
        else:
            break_car = hap.count('X')
            if break_car == 0:
                a[0] += 1
            elif break_car == 1:
                a[1] += 1
            elif break_car == 2:
                a[2] += 1
            elif break_car == 3:
                a[3] += 1
            elif break_car == 4:
                a[4] += 1

print(a[0])
print(a[1])
print(a[2])
print(a[3])
print(a[4])