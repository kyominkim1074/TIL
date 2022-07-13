
# a, b, c = input().split()
# a = int(a)  #변수 a에 저장되어있는 값을 정수로 바꾸어 다시 변수 a에 저장
# b = int(b)
# c = int(c)

# d = a if a<b else b
# e = d if d<c else c

# print(e)

a, b, c = map(int,input().split())
if a>b and c>b:
    print(b)
elif b>a and c>a:
    print(a)
else:
    print(c)
    
# split의 결과를 매번 int로 변환해주려니 귀찮습니다. 이때는 map을 함께 사용하면 됩니다.
# map에 int와 input().split()을 넣으면 split의 결과를 모두 int로 변환해줍니다(실수로 변환할 때는 int 대신 float를 넣습니다.).