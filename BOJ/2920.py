da = list(map(int, input().split()))

if da == sorted(da): #오름차순 (1234)
    print('ascending')
elif da == sorted(da, reverse=True): #내림차순(4321)
    print('descending')
else:
    print('mixed')