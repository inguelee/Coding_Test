N, K = map(int, input().split())
result = 0

while N >= K:
    c = N % K
    N -= c
    result += c

    N //= K
    result += 1

result += (N - 1)


print(result)