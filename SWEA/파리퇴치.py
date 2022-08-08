n = 5
m = 2
최대영역합 = 0

for 기준행 in range(n - m + 1):
    for 기준열 in range(n - m + 1):
        
        영역합 = 0
        for 행 in range(기준행, 기준행 + m):
            for 열 in range(기준열, 기준열 + m):
                영역합 += list_[행][열]
                
        if 영역합 > 최대영역합:
            최대영역합 = 영역합
            
            
print(최대영역합)