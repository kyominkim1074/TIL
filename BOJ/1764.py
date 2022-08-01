import sys
input=sys.stdin.readline
# n, m = map(int,input().split())
# dict_={}
# dict_['ohhernrie'] = '듣'
# dict_['charlie'] = '듣'
# dict_['baesangwook'] = '듣'

# if 'obama' in dict_:
#     print('obama 듣보잡')
# if 'baesangwook' in dict_:
#     print('baesangwook 듣보잡')
# if 'ohhernrie' in dict_:
#     print('obama 듣보잡')
# if 'clinton' in dict_:
#     print('obama 듣보잡')
    

# n, m = list(map(int,input().split()))
# dict_={}

# for i in range(n):
#     p = input()
#     dict_[p] = '듣'

# list_=[]
# for i in range(m):
#     p = input()
#     if p in dict_:
#         list_.append(p)

# list_.sort()
# print(len(list_))
# for p in list_:
#     print(p)

n, m = map(int, input().split())
d = dict()
l = []
for i in range(n):
    a = input()
    d[a] = '듣'
    
for j in range(m):
    a = input()
    if a in d.keys():
        l.append(a)
    else:
        d[a]='듣'
        
l.sort()
print(len(l))
for i in range(len(l)):
    print(l[i])