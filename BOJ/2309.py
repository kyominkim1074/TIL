import sys
input = sys.stdin.readline

n = [int(input()) for _ in range(9)]
hap = sum(n) # 난쟁이 아홉명의 키의 합
del_1 = 0 # 가짜 난쟁이 2명의 변수
del_2 = 0

for i in range(9): #이중 for문은 버려질 2명의 값을 의미한다.
    for j in range(i+1, 9):
        #9명의 키의 합에서 버릴 2명의 키를 빼서 100이 될 경우
        if hap - (n[i]+n[j]) == 100:
            #두 변수에 2명의 값을 대입한다.
            del_1 = n[i]
            del_2 = n[j]
            break

# 2명을 리스트에서 제거를 한 다음 정렬을 시킨 후에 차례대로 출력시킨다.
n.remove(del_1)
n.remove(del_2)
n.sort()

for i in n:
    print(i)