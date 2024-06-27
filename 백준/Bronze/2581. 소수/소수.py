from sys import stdin
import math

M = int(stdin.readline().strip())
N = int(stdin.readline().strip())

data = []
def sosu(n):
    if n == 1:
        return False
    for i in range(2, int(math.sqrt(n)) + 1):
        if n % i == 0:
            return False
        
    return True

for i in range(M, N + 1):
    if sosu(i):
        data.append(i)

if data:
    print(sum(data))
    print(min(data))
else:
    print(-1)