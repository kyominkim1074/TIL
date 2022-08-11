import sys
sys.stdin = open('1063.txt')
input = sys.stdin.readline

moving={'R':(0,1),
        'L':(0,-1),
        'T':(-1,0),
        'B':(1,0),
        'RT':(-1,1),
        'LT':(-1,-1),
        'RB':(1,1),
        'LB':(1,-1),
        }

king, dol, n = input().split()
kx, ky = 8-int(king[1]),ord(king[0])-65 #king x,y
dolx, doly = 8-int(dol[1]),ord(dol[0])-65 #dol x,y

for _ in range(int(n)):
    move = input().strip()
    dx, dy = moving[move]
    if not (0<=kx+dx<8 and 0<=ky+dy<8):
        continue
    ky+=dy
    kx+=dx
    if (kx, ky) == (dolx, doly):
        if not (0<=dolx+dx<8 and 0<=doly+dy<8):
            kx-=dx
            ky-=dy
            continue
        dolx += dx
        doly += dy
        
print(chr(ord('A')+ky)+str(8-kx))
print(chr(ord('A')+doly)+str(8-dolx))