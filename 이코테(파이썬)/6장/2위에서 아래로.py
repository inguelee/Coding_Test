N = int(input())
data = []

for i in range(N):
    data.append(int(input()))

data.sort(reverse=True)

for i in data:
    print(i, end=' ')
