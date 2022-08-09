import sys
input = sys.stdin.read

al = 'abcdefghijklmnopqrstuvwxyz'
r = []
s = input()

for i in al:
    r.append(s.count(i))
    
m = max(r)
for i in range(len(r)):
    if m == r[i]:
        print(chr(i+97), end='')