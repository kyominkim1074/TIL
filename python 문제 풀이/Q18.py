word='banana'
a={}

for i in word:
    if i in a:
        a[i] += 1
    else:
        a[i] = 1
for i in a:
    print(i, a[i])