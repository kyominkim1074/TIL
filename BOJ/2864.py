a, b = input().split()

min_n = int(a.replace('6', '5')) + int(b.replace('6', '5'))
max_n = int(a.replace('5', '6')) + int(b.replace('5', '6'))

print(min_n, max_n)