n = input()

n = int(n)

if n<0:
    if n%2 == 0:
        print("A")
    else:
        print("B")
if n>0:
    if n%2 == 0:
        print("C")
    else:
        print("D")

n = input()

n = int(n)

if (n<0) and (n%2 == 0):
    print("A")
else:
    if (n<0) and (n%2 != 0):
        print("B")
    elif (n>0) and (n%2 == 0): 
        print("C")
    else:
        print("D")