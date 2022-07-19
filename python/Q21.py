a = int(input())
re = 0
while(a > 0):
    b = a % 10
    re = (re * 10) + b
    a = a // 10
print('%d' %re)