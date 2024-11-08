from sys import stdin

array = []

for i in range(int(stdin.readline().strip())):
    a = stdin.readline().strip()
    if len(a) > 1:
        a, b = map(int, a.split())
    else:
        a = int(a)
    if a == 1:
        array.append(b)
    elif a == 2:
        if array:
            print(array.pop())
        else:
            print(-1)
    elif a == 3:
        print(len(array))
    elif a == 4:
        if array:
            print(0)
        else:
            print(1)
    elif a == 5:
        if array:
            print(array[-1])
        else:
            print(-1)