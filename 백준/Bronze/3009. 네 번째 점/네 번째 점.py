from sys import stdin

list_x = [0 for _ in range(1001)]
list_y = [0 for _ in range(1001)]

for _ in range(3):
    x, y = map(int, stdin.readline().strip().split())
    list_x[x] += 1
    list_y[y] += 1

print(list_x.index(1), list_y.index(1))