t = int(input())
for tc in range(1, t+1):
    
    a = input()
    y = int(a[:4])
    m = int(a[4:6])
    d = int(a[6:8])
    md = {1:31, 2:28, 3:31, 4:30, 5:31, 6:30, 7:31, 8:31, 9:30, 10:31, 11:30, 12:31}
    
    if (int(m)>=13) or (int(m)<=0): # month가 13이상 0이하일 때
        print(f"#{tc} -1")
    else:
        if md[int(m)] < int(d) or int(d) <= 0: #d값이 m에 지정된 날짜보다 크거나 0이하일 때
            print(f"#{tc} -1")
        else:
            print(f"#{tc} %04d/%02d/%02d" %(y,m,d))
