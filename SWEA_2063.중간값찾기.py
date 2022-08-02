N = int(input())
n = list(map(int, input().split()))
n.sort()
print(n[int((N-1)/2)])