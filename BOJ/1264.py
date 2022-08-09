import sys
input = sys.stdin.readline

value_ = ['a', 'e', 'i', 'o', 'u']

while True:
    word = list(input().lower())
    cnt = 0
    if word[0] == '#':
        break
    for i in word:
        if i in value_:
            cnt += 1
    print(cnt)