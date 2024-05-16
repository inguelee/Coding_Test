from itertools import combinations

N, M = map(int, input().split())
K = list(map(int, input().split()))
result = 0

for i in list(combinations(K, 2)):
    if i[0] != i[1]:
        result += 1

print(result)