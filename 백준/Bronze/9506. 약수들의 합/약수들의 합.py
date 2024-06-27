from sys import stdin

n = int(stdin.readline().strip())
while n != -1:
    b = 0
    data = [1]
    for i in range(2, n):
        if n % i == 0:
            data.append(i)

    if sum(data) == n:
        print(n, '=', data[0], end=' ')
        for i in data[1:]:
            print('+', i, end=' ')
        print()
    else:
        print(n,'is NOT perfect.')
    n = int(stdin.readline().strip())