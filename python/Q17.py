a='banana'
b=''

for i in range(len(a)):
    if (a[i] >= 'a' and  a[i] <='z'):
        b=b+chr((ord(a[i])-32))
    else:
        b=b+a[i]
print(b)