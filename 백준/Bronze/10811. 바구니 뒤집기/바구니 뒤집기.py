from sys import stdin

N, M = map(int, stdin.readline().strip().split())

data = [i for i in range(1, N + 1)]

for _ in range(M):
    a, b = map(int, stdin.readline().strip().split())
    big, low = max(a, b), min(a, b)
    while low < big:
        data[low-1], data[big-1] = data[big-1], data[low-1]
        big -= 1
        low += 1

for i in data:
    print(i, end=' ')