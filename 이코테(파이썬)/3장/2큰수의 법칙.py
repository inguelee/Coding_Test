N, M, K = map(int, input().split())
data = list(map(int, input().split()))

data.sort()
a = M // (K + 1)
b = M - a

result = (data[-2] * a) + (data[-1] * b)

print(result)