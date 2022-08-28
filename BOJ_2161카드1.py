N = int(input())
L = [num for num in range(1, N+1)]

out = []                   # 버린 카드 리스트
while len(L) > 1:          # L리스트에 마지막 하나 남을 때까지
    out.append(L.pop(0))   # 첫번째 카드 버리고, out리스트에 append
    L.append(L.pop(0))     # 다음 카드 맨뒤로 순서 옮기기

out.append(L.pop(0))       # 마지막 남은 카드 out 리스트에 append
print(*out)