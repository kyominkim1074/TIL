s = [input() for i in range(5)]

for i in range(15):
    for j in range(5):
        if i < len(s[j]):
            print(s[j][i], end='')