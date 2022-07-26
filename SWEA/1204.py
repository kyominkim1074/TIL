import sys
from typing import Counter
sys.stdin = open("input1204.txt")

t = int(input())
for tc in range(1, t+1):
    num = int(input())
    arr = list(map(int, input().split()))
    cnt = Counter(arr).most_common()