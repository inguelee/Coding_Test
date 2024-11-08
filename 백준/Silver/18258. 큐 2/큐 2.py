from sys import stdin
from collections import deque

array = deque()

for i in range(int(stdin.readline().strip())):
    a = stdin.readline().strip()
    if a[:4] == 'push':
        b = a.split()
        array.append(int(b[-1]))
    elif a == "front":
        if array:
            print(array[0])
        else:
            print(-1)
    elif a == "back":
        if array:
            print(array[-1])
        else:
            print(-1)
    elif a == "size":
        print(len(array))
    elif a == "empty":
        if array:
            print(0)
        else:
            print(1)
    elif a == "pop":
        if array:
            print(array.popleft())
        else:
            print(-1)
