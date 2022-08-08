delta_y = [0, 0, 1, -1]
delta_x = [1, -1, 0, 0]
y, x = 1, 1
for d in range(4):
    yy = y + delta_y[d]
    xx = x + delta_x[d]
    print(yy, xx)