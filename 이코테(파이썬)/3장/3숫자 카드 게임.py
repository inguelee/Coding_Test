N, M = map(int, input().split())

result = 0

for _ in range(N):
    value = min(map(int, input().split()))
    result = max(value, result)

print(result)