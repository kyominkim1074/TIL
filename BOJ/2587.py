import sys
input = sys.stdin.readline

list_ = []
for _ in range(5):
    n = int(input())
    list_.append(n)

average = sum(list_)//5
list_.sort()
print(average)
print(list_[2])