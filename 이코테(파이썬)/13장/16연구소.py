from itertools import combinations

N, M = map(int, input().split())
graph = []
cp = [[0] * M for _ in range(N)]
v = []
emp = []
for i in range(N):
    graph.append(list(map(int, input().split())))
    for j in range(M):
        if graph[i][j] == 2:
            v.append((i, j))
        elif graph[i][j] == 0:
            emp.append((i, j))
        cp[i][j] = graph[i][j]

dx = (-1,0, 1, 0)
dy = (0, 1, 0,-1)
#     북,동,남,서

def dfs(x, y):
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        if 0 <= nx < N and 0 <= ny < M:
            if graph[nx][ny] == 0:
                graph[nx][ny] = 2
                dfs(nx, ny)

result = 0

for i in list(combinations(emp, 3)):
    c = 0
    for x, y in i:
        graph[x][y] = 1
    for x, y in v:
        dfs(x, y)
    for x in range(N):
        for y in range(M):
            if graph[x][y] == 0:
                c += 1
    result = max(result, c)
    for x in range(N):
        for y in range(M):
            graph[x][y] = cp[x][y]

print(result)