cnt = 0                                 # 결과값을 받을 변수 cnt
for i in range(8):
    chess = list(input())               # 한 줄씩 입력받음
    if i % 2 == 0:                      # 짝수번째는 짝수번째가 하얀 칸
        cnt += chess[::2].count('F')    # 짝수번째에 있는 F count
    else:                               # 홀수번째
        cnt += chess[1::2].count('F')   # 홀수번째에 있는 F count

print(cnt)                              # 결과값 출력
