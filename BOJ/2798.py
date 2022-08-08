import sys
input = sys.stdin.readline

n, m = map(int, input().split())
card_n = list(map(int, input().split()))
total = 0

for i in range(n-2):
    for j in range(i+1, n-1):
        for k in range(j+1, n):
            sum_ = card_n[i]+card_n[j]+card_n[k]
            if sum_ > total and sum_ <= m:
                total = sum_
print(total)