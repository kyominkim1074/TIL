N = int(input())
n_list = map(int, input().split())
M = int(input())
m_list = map(int, input().split())

cnt = {}
# 카드의 숫자와 개수를 딕셔너리에 담는다.
for card in n_list:
    if card in cnt:
        cnt[card] += 1
    else:
        cnt[card] = 1
#딕셔너리에 {숫:개, 숫:개 ..... 숫:개} 이렇게 담겨지게 된다.

# 숫자카드 M을 딕셔너리의 키값을 찾아 value값을 출력하고
# 키값이 없으면 0으로 출력한다.
for target in m_list:
    if target in cnt:
        print(cnt[target], end=' ')
    else:
        print(0, end=' ')