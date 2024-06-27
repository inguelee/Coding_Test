from sys import stdin

N = int(stdin.readline().strip())

for i in range(2, N + 1):
    while N % i == 0:
        N //= i
        print(i)
    if N <= 1:
        break