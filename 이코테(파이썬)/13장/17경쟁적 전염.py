from collections import deque

N, K = map(int, input().split())
data = []
graph = []
for i in range(N):
    d = list(map(int, input().split()))
    for j in range(N):
        if d[j]:
            graph.append((d[j], 0, i, j))
    data.append(d)
S, X, Y = map(int, input().split())

dx = (-1,0, 1, 0)
dy = (0, 1, 0,-1)
#     북,동,남,서
graph.sort()
q = deque(graph)
while q:
    v, s, x, y = q.popleft()
    if s == S:
        break

    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        if 0 <= nx < N and 0 <= ny < N:
            if data[nx][ny] == 0:
                data[nx][ny] = v
                q.append((v, s + 1, nx, ny))

print(data[X - 1][Y - 1])