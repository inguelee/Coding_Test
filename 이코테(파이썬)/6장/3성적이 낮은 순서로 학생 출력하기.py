N = int(input())
data = []
for _ in range(N):
    a, b = input().split()
    b = int(b)
    data.append([a, b])

def setting(data):
    return data[1]

data.sort(key=setting)

for i in data:
    print(i[0], end=' ')