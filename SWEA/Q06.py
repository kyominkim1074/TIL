s = list(input())

for i in s:
    a = ord(i)-64
    print(a, end=' ')
    
#알파벳을 아스키코드 변환 함수로 바꿔주면 됨
#문자열 - 아스키 : ord
#아스키 - 문자열 : chr