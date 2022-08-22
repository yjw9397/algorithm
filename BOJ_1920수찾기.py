# 이진 탐색으로 안 풀면 시간 초과 나옴!

import sys

N = int(sys.stdin.readline())
A = list(map(int, sys.stdin.readline().split()))
M = int(sys.stdin.readline())
num = list(map(int, sys.stdin.readline().split()))

A.sort()
for i in num:
    left = 0
    right = N - 1
    while left <= right:
        middle = (left + right) // 2
        if A[middle] == i:
            print(1)
            break
        elif i < A[middle]:
            right = middle - 1
        elif i > A[middle]:
            left = middle + 1
    else:
        print(0)