T = int(input())
for tc in range(1, T+1):
    h1, m1, h2, m2 = map(int, input().split())
    
    H = h1 + h2
    M = m1 + m2
    if H >=13: #시간을 더했을 때
        H -= 12 # 12를 빼준다
    if M > 59:  #분 합이 60이상이면
        M -= 60 #60을 빼주고
        H += 1 #시간을 1추가
    print(f'#%d' %tc, H, M)