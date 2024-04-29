N, M, K = map(int, input().split())
data = sorted(list(map(int, input().split())))

S1 = M // (K + 1)

result = (data[-1] * (M - S1)) + (S1 * data[-2])
print(result)