from sys import stdin

data = [[0 for i in range(100)] for i in range(100)]
result = 0

for _ in range(int(stdin.readline())):
    a, b = map(int, stdin.readline().split())
    for i in range(a, a + 10):
        for j in range(b, b + 10):
            data[i][j] = 1

for i in data:
    if 1 in i:
        result += i.count(1)

print(result)