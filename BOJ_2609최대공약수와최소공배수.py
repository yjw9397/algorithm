a, b = map(int, input().split())

for i in range(min(a, b), 0, -1):   # 값이 더 빨리 나오게하기 위해 range -1
    if a % i == 0 and b % i == 0:
        M = i                       # 최대공약수
        break

m = M * (a//M) * (b//M)             # 최소공배수

print(M)
print(m)


# 유클리드 호제법 풀이 방식
def gcd(M, m):
    if m == 0:
        return M
    else:
        return gcd(m, M % m)

a, b = map(int, input().split())
g = gcd(a, b)
print(g)
print(a * b // g)