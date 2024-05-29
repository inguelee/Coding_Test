from itertools import combinations
from collections import deque

N, M = map(int, input().split())
graph = []
emp = []
v = []
cp = [[0] * M for _ in range(N)]
for i in range(N):
    graph.append(list(map(int, input().split())))
    for j in range(M):
        cp[i][j] = graph[i][j]
        if graph[i][j] == 0:
            emp.append((i, j))
        elif graph[i][j] == 2:
            v.append((i, j))

dx = (-1,0, 1, 0)
dy = (0, 1, 0,-1)
c, result = 0, 0
#     북,동,남,서

def virus(x, y):
    q = deque()
    q.append((x, y))
    while q:
        x, y = q.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx < N and 0 <= ny < M:
                if graph[nx][ny] == 0:
                    graph[nx][ny] = 2
                    q.append((nx, ny))

for i in list(combinations(emp, 3)):
    for x, y in i:
        graph[x][y] = 1
    for x, y in v:
        virus(x, y)
    for x in range(N):
        for y in range(M):
            if graph[x][y] == 0:
                c += 1
    result = max(result, c)
    for x in range(N):
        for y in range(M):
            graph[x][y] = cp[x][y]
    c = 0

print(result)