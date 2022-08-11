import sys
sys.stdin = open('2857.txt')
input = sys.stdin.readline

data = [input() for _ in range(5)]
agent = 0
for i in range(len(data)):
    if 'FBI' in data[i]:
        print(i+1, end=' ')
        agent=1

if agent==0:
    print('HE GOT AWAY!')