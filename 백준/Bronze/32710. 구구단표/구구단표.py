from sys import stdin

array = set()

for i in range(1, 10):
    for j in range(1, 10):
        array.add(i * j)

n = int(stdin.readline().strip())
print(int(n in array))