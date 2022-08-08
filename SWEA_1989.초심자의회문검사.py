T = int(input())

for i in range(T):
    word = input()
    if word == word[::-1]:
        result = 1
    else:
        result = 0
    print(f'#{i+1} {result}')