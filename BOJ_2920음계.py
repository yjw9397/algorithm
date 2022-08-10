A = [1, 2, 3, 4, 5, 6, 7, 8]
L = list(map(int, input().split()))

if L == A:
    print('ascending')
elif L == A[::-1]:
    print('descending')
else:
    print('mixed')