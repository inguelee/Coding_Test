from sys import stdin

N, K = map(int, stdin.readline().strip().split())

array = [i for i in range(1, N + 1)]

n = 0

print('<', end='')

n += K - 1
while len(array) <= n:
    n %= len(array)
print(array.pop(n), end='')

while array:
    print(', ', end='')
    n += K - 1
    while len(array) <= n:
        n %= len(array)
    print(array.pop(n), end='')

print('>')