T = int(input())
for test_case in range(1, T + 1):
    
    a, b, c, d, e, f, g, h, i, j = map(int, input().split())
    q = (a + b + c + d + e + f + g + h + i + j)/10
    r = round(q)

    print("#{} {}".format(test_case, r))