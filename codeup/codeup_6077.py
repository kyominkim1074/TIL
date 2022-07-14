n = int(input())
s = 0
for i in range(1, n+1) :
  if i%2!=1 :
    s += i
print(s)

a = int(input())
b = 0
c = 1
while c < a:
  if c%2 != 1:
    b += c
  else:
    pass
  c=c+1
print(b)