n = int(input())
s = n
cnt = 0

while True:
    a = s//10
    b = s%10
    c = (a+b)%10
    s = (b*10)+c
    
    cnt+=1
    if (s == n):
        break

print(cnt)

