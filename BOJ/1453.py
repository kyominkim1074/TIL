import sys
input = sys.stdin.readline

n = int(input())
zari = [0]*101 # pc방의 빈 자리 100석
pc_bang = list(map(int, input().split())) #손님이 원하는 자리 번호
cnt = 0

#100석의 자리 중에 손님이 원하는 자리가 빈 자리
#즉 값이 0인 경우 그 자리의 값을 1로 바꾼다.
for i in pc_bang:
    if zari[i] == 0:
        zari[i] = 1
#0이 아닌 경우 자리가 있는경우이기 때문에 거절당하는 사람의 수
#cnt의 값에 1 더한다
    else:
        cnt += 1
        
print(cnt)