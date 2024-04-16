N, M, K = map(int, input().split())
data = list(map(int, input().split()))
data.sort()
result = 0
for i in range(M):
    if K % (i + 1):
        result += data[-1]
    else:
        result += data[-2]

print(result)