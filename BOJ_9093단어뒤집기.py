T = int(input())

for t in range(T):
    L = input()
    for a in L.split(' '):
        print(a[::-1], end=' ')

'''
import sys
input = sys.stdin.readline

for t in range(int(input())):
로 하면 시간 단축!
'''