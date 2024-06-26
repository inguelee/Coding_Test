from sys import stdin

data = [1,1,2,2,2,8]

sub = tuple(map(int, stdin.readline().strip().split()))


for i in range(6):
    data[i] = data[i] - sub[i]

for i in data:
    print(i, end=' ')