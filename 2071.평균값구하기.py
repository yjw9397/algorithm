T = int(input())

for i in range(0, T):
    j = list(map(int, input().split()))
    num = i + 1
    av = round(sum(j)/10)
    print(f'#{num} {av}')