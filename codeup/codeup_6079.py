a = int(input())
b=0
c=0
while c<a:
    b+=1
    c+=b
print(b)

# 정수 a를 int형으로 입력받습니다.
# 그리고 while 반복문으로 total(c)이라는 변수가 입력받은 정수 a보다 커지기 전까지 계속 반복합니다.
# 반복문 안에서는 b를 증가시키고 증가시킨 b 만큼 total(c)에 더해줍니다.
# 마지막에 더한 b가 마지막에 더한 정수가 되므로 while 반복문이 끝나고 나면 print() 함수로 b를 출력해줍니다.