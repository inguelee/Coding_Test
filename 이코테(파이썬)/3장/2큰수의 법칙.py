N, M, K = map(int, input().split())
data = list(map(int, input().split()))

data.sort()

c = M // (K + 1)

result = ((M - c) * data[-1]) + data[-2] * c
print(result)