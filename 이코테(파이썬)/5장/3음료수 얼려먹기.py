N, M = map(int, input().split())
graph = []
for _ in range(N):
    graph.append(list(map(int, input())))

result = 0
dx = (-1,0, 1, 0)
dy = (0, 1, 0,-1)
#     북,동,남,서

def dfs(x, y):
    if 0 <= x < N and 0 <= y < M:
        if graph[x][y]:
            return False
        else:    
            graph[x][y] = 1
            for i in range(4):
                nx = x + dx[i]
                ny = y + dy[i]
                dfs(nx, ny)
            return True

for i in range(N):
    for j in range(M):
        if dfs(i, j):
            result += 1

print(result)