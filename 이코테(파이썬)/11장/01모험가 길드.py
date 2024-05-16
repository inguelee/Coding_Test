N = int(input())
data = list(map(int, input().split()))

data.sort()
result = 0

for i in set(data):
    result += (data.count(i) // i)

print(result)