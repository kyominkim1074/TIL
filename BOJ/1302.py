import sys
input=sys.stdin.readline
t = int(input())
books = {}

for b in range(t):
    book = input()
    if book not in books:
        books[book] = 1
    else:
        books[book] += 1
maax = 0
best = dict(sorted(books.items()))

for i in best:
    if (best[i]) > maax:
        maax=best[i]
        max = i
print(max)