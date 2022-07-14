#1
numbers = [0, 20, 100]
a=numbers[2]
b=numbers[0]
for i in numbers:
    if i>a:
        b=i
        a=i
    elif i>b and i!=a:
        b=i
print(b)

#2
numbers = [0, 20, 100, 50, -60, 50, 100]
a=numbers[2]
b=numbers[0]
for i in numbers:
    if i>a:
        b=i
        a=i
    elif i>b and i!=a:
        b=i
print(b)
#3
numbers = [0, 1, 0]
a=numbers[1]
b=numbers[0]
for i in numbers:
    if i>a:
        b=i
        a=i
    elif i>b and i!=a:
        b=i
print(b)

#4
numbers = [-10, -100, -30]
a=numbers[0]
b=numbers[1]
for i in numbers:
    if i>a:
        b=i
        a=i
    elif i>b and i!=a:
        b=i
print(b)