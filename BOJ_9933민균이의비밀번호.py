N = int(input())
pw = [input() for _ in range(N)]
for word in pw:
    if word[::-1] in pw:
        print(len(word), word[(len(word)-1)//2])
        break  # 안 할 경우 2번 출력됨