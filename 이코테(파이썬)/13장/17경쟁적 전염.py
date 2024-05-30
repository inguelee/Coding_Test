from collections import deque

N, K = map(int, input().split())
graph = []
q = []
for i in range(N):
    graph.append(list(map(int, input().split())))
    for j in range(N):
        if graph[i][j]:
            q.append((graph[i][j], 0, i, j))
S, X, Y = map(int, input().split())

q.sort()
dx = (-1,0, 1, 0)
dy = (0, 1, 0,-1)
q = deque(q)

while q:
    v, s, x, y = q.popleft()
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        if 0 <= nx < N and 0 <= ny < N:
            if graph[nx][ny] == 0:
                graph[nx][ny] = v
                q.append((v, s + 1, nx, ny))

    if s == (S - 1):
        break

print(graph[X - 1][Y - 1])