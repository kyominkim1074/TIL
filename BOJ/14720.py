# 처음에는 딸기우유를 한 팩 마신다.
# 딸기우유를 한 팩 마신 후에는 초코우유를 한 팩 마신다.
# 초코우유를 한 팩 마신 후에는 바나나우유를 한 팩 마신다.
# 바나나우유를 한 팩 마신 후에는 딸기우유를 한 팩 마신다. 
# 우유 가게는 딸기, 초코, 바나나 중 한종류만 취급
# 우유 가게 앞에서 우유를 사마시거나 사마시지 않는다
# 한 번 지나친 가게는 다시 안 간다
# 첫 째 줄에 가게의 수
# 둘째 줄에는 우유 가게 정보가 우유 거리의 시작부터 끝까지
# 순서대로 N개의 정수로 주어진다.
# 0 = 딸기 1 = 초코 2 = 바나나
# 0,1,2 이외의 숫자는 주어지지 않는다.

n = int(input())
a = list(map(int, input().split()))
cnt = 0

for i in range(n):
    if a[i] == cnt % 3:
        cnt += 1
print(cnt)