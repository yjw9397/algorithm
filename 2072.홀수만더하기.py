T = int(input())


for i in range(0, T):
    j = map(int, input().split())
    a = []
    for num in j:
        if num % 2 != 0:
            a.append(num)
    print(f'#{i+1} {sum(a)}')