from sys import stdin
from collections import deque

d = deque()

for _ in range(int(stdin.readline().strip())):
    c = stdin.readline().strip().split()
    a = int(c[0])
    if a == 1:
        d.appendleft(int(c[-1]))
    elif a == 2:
        d.append(int(c[-1]))
    elif a == 3:
        if d:
            print(d.popleft())
        else:
            print(-1)
    elif a == 4:
        if d:
            print(d.pop())
        else:
            print(-1)
    elif a == 5:
        print(len(d))
    elif a == 6:
        if d:
            print(0)
        else:
            print(1)
    elif a == 7:
        if d:
            print(d[0])
        else:
            print(-1)
    elif a == 8:
        if d:
            print(d[-1])
        else:
            print(-1)