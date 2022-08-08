h, m = map(int, input().split())
T = int(input())

if m + T % 60 < 60:
    if h + T //60 < 24:
        print(h + T // 60, m + T % 60)
    else:
        print(h + T // 60 - 24, m + T % 60)
else:
    if h + T //60 < 23:
        print(h + T // 60 + 1, m + T % 60 - 60)
    else:
        print(h + T // 60 - 23, m + T % 60 - 60)

# m + T를 먼저 하면 더 연산이 짧아짐!