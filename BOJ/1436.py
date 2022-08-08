import sys
input = sys.stdin.readline

n = int(input())
number = 666
cnt = 0

while True:
    if '666' in str(number): # 숫자에 666이 포함되어 있는 경우
        cnt += 1 # cnt 값에 1 더한다
    if cnt == n: #cnt 값이 n의 값과 같을 경우 while반복문을 끝낸다.
        print(number)
        break
    number += 1 # 반복문이 끝날 때까지 매번 사이클 마다 1씩 더해준다.