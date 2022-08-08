N = int(input())

for i in range(N):
    print(' '*(i) + '*'*(2*(N-i)-1))
for i in range(N-2, -1, -1):
    print(' '*(i) + '*'*(2*(N-i)-1))

# 괜히 뒤에 공백까지 찍어서 출력 형식 잘못되었다고 나왔었음