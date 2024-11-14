from sys import stdin
from collections import deque

N = int(stdin.readline().strip())

array = [i for i in range(1, N + 1)]
array = deque(array)

print(array.popleft(), end=' ')
while array:
    array.append(array.popleft())
    print(array.popleft(), end=' ')