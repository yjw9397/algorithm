word = input()

#아스키코드를 활용하여 변경
for a in word:
    if ord('D') <= ord(a) <= ord('Z'):
        a = chr(ord(a)-3)
    elif ord(a) < ord('D'):                     #'A', 'B', 'C' 예외
        a = chr(ord(a) + (ord('X')-ord('A')))   #'A' -> 'X'가 되므로 그 차이만큼 더해줌
    print(a, end='')