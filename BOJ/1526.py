import sys
input = sys.stdin.readline

n = int(input())
while 1:
    cnt=0
    for i in str(n):
        if i!='4' and i!='7':
            cnt=1
            n-=1
    if cnt==0:
        print(n)
        break
    
    
# 숫자 N 입력
N = int(input())

# 초기 가장 큰 값 N은 4 이상
max_ = 4

for number in range(N + 1):
    # 숫자를 문자열로 변환
    string_number = str(number)

    # 각 숫자의 자릿수 값 확인
    for char_number in string_number:
        # 각 자릿수가 4 또는 7로만 이루어져있는 확인
        # 각 자릿수가 4 또는 7로만 이러어져있지 않으면 반복을 멈추면 된다. break
        if not (char_number == "4" or char_number == "7"):
            break

    # for ~ else ~
    # for이 정상적으로 다 완료되면 else가 실행된다.
    # break를 만나지 않으면 else가 실행된다.
    else:
        # 최댓값을 갱신, 비교 X
        # 숫자는 계속해서 커지기 때문에 비교 X
        max_ = int(string_number)

print(max_)