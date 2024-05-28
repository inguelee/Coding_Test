from collections import deque

N, M = map(int, input().split())
data = []
for _ in range(N):
    data.append(list(map(int, input())))

dx = (-1,0, 1, 0)
dy = (0, 1, 0,-1)
#     북,동,남,서

def bfs():
    q = deque()
    q.append((0, 0))
    while q:
        x, y = q.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx < N and 0 <= ny < M:
                if data[nx][ny] == 1: # 한번도 안가본 길
                    q.append((nx, ny))
                    data[nx][ny] = data[x][y] + 1

    return data[N - 1][M - 1]
            

print(bfs())