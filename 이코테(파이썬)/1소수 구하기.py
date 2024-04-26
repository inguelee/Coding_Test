import math

M, N = map(int, input().split())
result = []

def sw(n):
    for i in range(2, int(math.sqrt(n)) + 1):
        if n % i == 0:
            return False
    return True

for i in range(M, N):
    if sw(i):
        result.append(i)

print(result)