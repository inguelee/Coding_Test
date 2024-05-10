from itertools import combinations

N, M = map(int, input().split())
k = list(map(int, input().split()))
result = []

# print(list(combinations(k, 2)))
for i in list(combinations(k, 2)):
    if i[0] != i[1]:
        result.append(i)

print(len(result))