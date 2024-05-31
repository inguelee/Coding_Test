N, M = map(int, input().split())
graph = list()
for _ in range(N):
    graph.append(list(map(int, input())))

result = 0

def dfs(x, y):
    if 0 <= x < N and 0 <= y < M:
        if graph[x][y]:
            return False
        else:
            graph[x][y] = 1
            dfs(x + 1, y)
            dfs(x, y + 1)
            dfs(x - 1, y)
            dfs(x, y - 1)
            return True
    return False

for i in range(N):
    for j in range(M):
        if dfs(i, j):
            result += 1

print(result)