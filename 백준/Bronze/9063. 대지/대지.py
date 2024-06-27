from sys import stdin

data = []

for _ in range(int(stdin.readline().strip())):
    data.append(tuple(map(int, stdin.readline().strip().split())))

sx = min(data)[0]
lx = max(data)[0]
sy = min(data, key=lambda x:x[1])[1]
ly = max(data, key=lambda x:x[1])[1]

x = lx - sx
y = ly - sy
print(x * y)