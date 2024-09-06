from sys import stdin

array = []
for i in range(5):
    array.append(int(stdin.readline().strip()))

array.sort()

print(sum(array) // 5)
print(array[2])