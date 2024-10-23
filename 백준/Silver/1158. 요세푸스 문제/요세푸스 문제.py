from sys import stdin

N, K = map(int, stdin.readline().strip().split())

n = K - 1
array = [i for i in range(1, N + 1)]
result = []

while sum(array):
    if array[n]:
        result.append(str(array.pop(n)))
        n += K - 1

    while len(array) and n >= len(array):
        n -= len(array)

print('<' + ', '.join(result) + '>')