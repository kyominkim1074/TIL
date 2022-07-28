import sys
input=sys.stdin.readline
t = int(input())
person = {}
for _ in range(t):
    p, com = input().split()
#com이 enter일 경우 해당되는 사람 이름을 키 값으로 한다.
    if com == 'enter':
        person[p] = 1
#leave의 경우에는 딕셔너리에서 지운다.
    else:
        del person[p]
#딕셔너리의 모든 키값을 역순으로 정렬한다.
for pp in sorted(person.keys(), reverse=True):
    print(pp)