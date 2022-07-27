n = list(range(1, 10001))
lis = [] #생성자

for num in n:
    for nn in str(num): #자리수 분산을 위해 str로 변경
        num += int(nn)
    if num <= 10000:
        lis.append(num)
for s in set(lis):
    n.remove(s)
for self_ in n:
    print(self_)