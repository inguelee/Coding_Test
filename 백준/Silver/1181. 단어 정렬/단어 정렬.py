from sys import stdin

array = []

for i in range(int(stdin.readline().strip())):
    array.append(stdin.readline().strip())

a = set(array)
b = list(a)
b.sort()
b.sort(key=lambda x:len(x))

for i in b:
    print(i)