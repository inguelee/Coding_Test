N, M = map(int, input().split())
data = []
for _ in range(N):
    data.append(list(map(int, input())))

graph = [[False] * M for _ in range(N)]
result = 0
x, y = 0, 0

def dfs(x, y):
    if 0 <= x < N and 0 <= y < M:
        if graph[x][y]:
            return False
        
        if data[x][y]:
            return False
        else:
            graph[x][y] = True
            dfs(x + 1, y)
            dfs(x, y + 1)
            dfs(x - 1, y)
            dfs(x, y - 1)
            return True
    else:
        return False

    

for i in range(N):
    for j in range(M):
        if dfs(i, j):
            result += 1

print(result)