N, K = map(int, input().split())

result = 0

while N >= K:
    c = N % K
    result += c
    N -= c

    N //= K
    result += 1

result += (N % K) - 1

print(result)