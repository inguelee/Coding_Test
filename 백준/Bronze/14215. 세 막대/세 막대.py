from sys import stdin

data = list(map(int, stdin.readline().strip().split()))

data.sort(reverse=True)
if data[0] >= sum([data[1], data[2]]):
    data[0] -= (data[0] - sum([data[1], data[2]])) + 1
    
print(sum(data))