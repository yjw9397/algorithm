N = int(input())
L = []  #파일 이름들을 받을 리스트 선언

#각 파일 이름을 받아 L리스트에 넣음
for _ in range(N):
    L.append(list(input()))

#L리스트에 있는 각 파일 이름들을 비교
for i in range(N-1):            #i와 i+1을 비교하므로 마지막 제외 범위 설정
    for j in range(len(L[0])):  #모든 파일 이름의 길이가 같으므로 len(L[0])로 범위 설정
        if L[i][j] != L[i+1][j]:
            L[i+1][j] = '?'     #i와 i+1의 j번째 문자가 다르다면 j번째 문자를 '?'로 변환
print(''.join(L[-1]))           #L리스트의 마지막 원소를 join하여 출력

''' 
- 파일 이름을 list형이 아니라 그냥 받을 경우, 문자 변환할 때 TypeError
(비교는 가능, 변환시 error)
- replace 함수 사용 시, 단어에 포함되어 있는 해당 문자 모두 변환됨
'''