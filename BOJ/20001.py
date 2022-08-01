s = input()
stack = []
while s != '고무오리 디버깅 끝':
    s = input()
    if s == '고무오리 디버깅 끝':
        break
    if s == '문제':
        stack.append(s)
    elif stack and s == '고무오리':
        stack.pop()
    else :
        stack.append('문제')
        stack.append('문제')

if stack:
    print('힝구')
else:
    print('고무오리야 사랑해')