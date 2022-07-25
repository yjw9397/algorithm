T = int(input())

for i in range(T):
    a, b = map(int, input().split())
    c = ''
    if a > b:
        c = '>'
    elif a < b:
        c = '<'
    else:
    	c = '='
    print(f'#{i+1} {c}')