#before
numbers = input().split()
print(sum(numbers))
#after
numbers = map(int, input().split())
print(sum(numbers))