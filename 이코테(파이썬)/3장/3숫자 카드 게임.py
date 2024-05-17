N, M = map(int, input().split())
result = 0
for _ in range(N):
    data = list(map(int, input().split()))
    value = min(data)
    result = max(value, result)

print(result)