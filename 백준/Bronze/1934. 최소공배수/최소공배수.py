import math
from sys import stdin

for _ in range(int(stdin.readline().strip())):
    A, B = map(int, stdin.readline().strip().split())
    print(math.lcm(A, B))