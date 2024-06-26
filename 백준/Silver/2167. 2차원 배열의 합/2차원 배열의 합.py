from sys import stdin

data = []
result = []
a, b = map(int, stdin.readline().strip().split())
for _ in range(a):
    data.append(tuple(map(int, stdin.readline().split())))
for _ in range(int(stdin.readline().strip())):
    i, j, x, y = map(int, stdin.readline().strip().split())
    s = 0
    for a in range(i-1, x):
        for b in range(j-1, y):
            s += data[a][b]
    
    result.append(s)

for i in result:
    print(i)