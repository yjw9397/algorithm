T  = int(input())
for _ in range(T):
    VPS = list(input())

    stack = []
    result = ''
    for i in VPS:
        if i == '(':
            stack.append(i)
        else:
            if not stack:       # i == ')'인데 stack이 False 인 경우
                stack = True # stack을 True로 바꾼 후 break(밑의 조건문을 고려)
                break
            stack.pop()
    if stack:                    # 예시가 끝났는데 stack이 True인 경우
        result = 'NO'         # NO
    else:                          # 아닌 경우
        result = 'YES'        # YES

    print(result)