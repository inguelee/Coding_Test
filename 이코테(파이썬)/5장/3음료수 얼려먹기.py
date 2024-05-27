N, M = map(int, input().split())
data = []
visited = [[False] * M for i in range(N)]
for _ in range(N):
    data.append(input())

def dfs(x, y):
    if 0 <= x < N and 0 <= y < M:
        if visited[x][y]:   # 이미 방문했으면 끝
            return False
        else:
            if data[x][y] == '0':
                visited[x][y] = True
                dfs(x + 1, y)
                dfs(x, y + 1)
                dfs(x - 1, y)
                dfs(x, y - 1)
                return True
            else:
                return False
    else:
        return False                            # 방문하지 않았다면

c = 0
for i in range(N):
    for j in range(M):
        if dfs(i, j):
            c += 1

print(c)