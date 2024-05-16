N, K = map(int, input().split())

result = 0

while N >= K:
    result += N % K
    N -= (N % K)
    
    N = N // K
    result += 1

result += (N % K) - 1
print(result)