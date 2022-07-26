T = int(input())

for i in range(0, T):
    j = list(map(int, input().split()))
    num = i + 1
    av = round(sum(j)/10)
    print(f'#{num} {av}')


'''
SWEA 2071. 평균값 구하기

- 10개의 수를 입력 받아, 평균값을 출력하는 프로그램을 작성(소수점 첫째 자리에서 반올림한 정수 출력)

- 가장 첫 줄: 테스트 케이스의 개수 T'
- 각 테스트 케이스의 첫 번째 줄에는 10개의 수
- #t'(테스트 케이스번호)로 시작, 공백을 한 칸 둔 다음 정답을 출력

[예시]
입력
3
3 17 1 39 8 41 2 32 99 2
22 8 5 123 7 2 63 7 3 46
6 63 2 3 58 76 21 33 8 1 

출력
#1 24
#2 29
#3 27
'''