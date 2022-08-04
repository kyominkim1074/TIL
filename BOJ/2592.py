import sys
input = sys.stdin.readline

number = [int(input()) for _ in range(10)]
print(sum(number)//10)
print(max(number, key = number.count))