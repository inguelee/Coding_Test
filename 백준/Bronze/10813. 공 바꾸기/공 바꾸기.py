from sys import stdin

N, M = map(int, stdin.readline().strip().split())

data = [i for i in range(1, N + 1)]

for _ in range(M):
    a, b = map(int, stdin.readline().strip().split())
    data[a-1], data[b-1] = data[b-1], data[a-1]

for i in data:
    print(i, end=' ')