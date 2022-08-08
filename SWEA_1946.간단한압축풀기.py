T = int(input())

for t in range(T):
    N = int(input())
    list_a = ''
    for i in range(N):
        a, num = input().split()
        for j in range(int(num)):
            list_a += a
    
    print(f'#{t+1}')
    k = 1        
    while k <= (len(list_a)//10 + 1):
        print(list_a[10*(k-1):10*k], end='\n')
        k += 1

'''
T = int(input()) #T 받은 후 for문 생성, 아래 전체 for문 안에 넣기
N = int(input())

list_a = ''
for i in range(N):
    a, num = input().split()
    for j in range(int(num)):
        list_a += a

print(f'#{T}') #T -> t+1
k = 1
while k <= N:  #N -> len(list_a)//10 + 1
    print(list_a[10*(k-1):10*k], end='\n')
    k += 1

# fail, 10개 테스트 케이스 중 3개 맞았다고 뜸
'''