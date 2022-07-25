n = int(input())
han = 0

for i in range(1, n+1):
    if i <= 99:
        han += 1
    else:
        nn = list(map(int, str(i)))
        if nn[0] - nn[1] == nn[1] - nn[2] :
            han += 1
print(han)