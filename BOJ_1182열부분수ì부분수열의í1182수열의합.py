# stack 부분집합 이용 풀이
N, S = map(int, input().split())
L = list(map(int, input().split()))

subsets = [[]]
for num in L:
    for i in range(len(subsets)):
        subsets.append(subsets[i] + [num])

cnt = 0
for i in subsets:
    if i and sum(i) == S:
        cnt += 1

print(cnt)
---------------------------------------------------------------------

# combinations 사용 풀이
from itertools import combinations

N, S = map(int, input().split())
L = list(map(int, input().split()))

cnt = 0
for i in range(1, N+1):
    for j in combinations(L, i):
        if sum(j) == S:
            cnt += 1

print(cnt)