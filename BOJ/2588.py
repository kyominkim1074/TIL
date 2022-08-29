import sys
sys.stdin = open('2588.txt')
input = sys.stdin.readline

n1=int(input())
n2=input()

n3=n1*int(n2[2])
n4=n1*int(n2[1])
n5=n1*int(n2[0])
n6=n1*int(n2)

print(n3, n4, n5, n6, sep='\n')