a = list(map(int, input().split()))
b = list(map(int, input().split()))
a_score = 0
b_score = 0
win = 'D' #기본적으로 draw로 기록

for round in range(10):
#승자는 3점 추가, 비길 경우에는 둘 다 1점씩
#이긴 쪽에 win변수를 기록해 둔다.
    if a[round] > b[round]:
        a_score+=3
        win = 'A'
    if a[round] < b[round]:
        b_score+=3
        win = 'B'
    if a[round] == b[round]:
        a_score+=1
        b_score+=1
        
if a_score > b_score:
    print(a_score, b_score)
    print('A')
if a_score < b_score:
    print(a_score, b_score)
    print('B')
    
# 둘 다 점수가 같은 경우
if a_score == b_score:
    if win == 'A': #win변수가 A인 경우
        print(a_score, b_score)
        print('A')
    if win == 'B': #win변수가 B인 경우
        print(a_score, b_score)
        print('B')
    if win =='D': #win변수가 D인 경우
        print(a_score, b_score)
        print('D')