from collections import deque

N, M, K, X = map(int, input().split())
graph = [[] for _ in range(N + 1)]
data = [i for i in range(N + 1)]
for i in range(M):
    a, b = map(int, input().split())
    graph[a].append(b)

d = [-1] * (N + 1)
d[X] = 0

q = deque()
q.append(X)
while q:
    x = q.popleft()
    for i in graph[x]:
        if d[i] == -1:
            d[i] = d[x] + 1
            q.append(i)

find = False
for i in range(1, N + 1):
    if d[i] == K:
        print(i)
        find = True

if find == False:
    print(-1)