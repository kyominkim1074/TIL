import sys
input = sys.stdin.readline

class_ = int(input())

for c in range(1, class_+1):
    test_score = list(map(int, input().split()))[1:]
    test_score.sort()
    gap = 0
    max_score = max(test_score)
    min_score = min(test_score)
    for i in range(len(test_score)-1):
        if gap < test_score[i+1] - test_score[i]:
            gap = test_score[i+1] - test_score[i]
    print(f'Class {c}')
    print(f'Max {max_score}, Min {min_score}, Largest gap {gap}')