N, K = map(int, input().split())
c = 0

while N != 1:
    if N % K:
        N -= 1
    else:
        N //= K
    c += 1

print(c)