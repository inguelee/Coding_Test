from sys import stdin

data = (1,1,2,2,2,8)

sub = tuple(map(int, stdin.readline().strip().split()))

result = [0] * 6

for i in range(6):
    result[i] = data[i] - sub[i]

for i in result:
    print(i, end=' ')