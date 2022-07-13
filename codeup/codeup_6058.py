a, b=input().split()
c = bool(int(a))
d = bool(int(b))
if bool(c) == False and bool(d)==False:
    print(True)
else:
    print(False)

a, b=input().split()
c = bool(int(a))
d = bool(int(b))
print((not c) or (not d))