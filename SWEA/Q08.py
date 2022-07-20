    # P = int(input()) #A사 리터당 요금
    # Q = int(input()) #B사 기본 요금
    # R = int(input()) #B사 기본요금 기준 수도 양
    # S = int(input()) #B사 리터당 추가 요금
    # W = int(input()) #한 달간 쓴 수도 양
T = int(input())
for case in range(1, T+1):
    P, Q, R, S, W = map(int, input().split())
    
    a = P * W
    if W < R:
        b = Q
    else:
        b = Q+(S*(W-R))
    print(f'#{case} {a if a < b else b}')
    # print(f'#{case} {min(a, b)}') 도 가능