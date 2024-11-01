from sys import stdin

N = int(stdin.readline().strip())

while N:
    s = 0
    while N % 10 or N > 0:
        a = N % 10
        N //= 10
        s += a
        if N % 10 == 0 and s // 10:
            N = s
            s = 0
    print(s)

    N = int(stdin.readline().strip())