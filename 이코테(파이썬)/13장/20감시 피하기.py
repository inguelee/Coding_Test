from itertools import combinations

N = int(input())
graph = []
t = []
s = []
x = []
for i in range(N):
    graph.append(list(input().split()))
    for j in range(N):
        if graph[i][j] == 'X':
            x.append((i, j))
        elif graph[i][j] == 'T':
            t.append((i, j))

def watch(x, y):
    xx, yy = x, y
    for i in range(4):
        if i == 0:
            while x >= 0:
                if graph[x][y] == 'S':
                    return False
                elif graph[x][y] == 'O':
                    return True
                x -= 1
        elif i == 1:
            while x < N:
                if graph[x][y] == 'S':
                    return False
                elif graph[x][y] == 'O':
                    return True
                x += 1
        elif i == 2:
            while y >= 0:
                if graph[x][y] == 'S':
                    return False
                elif graph[x][y] == 'O':
                    return True
                y -= 1
        elif i == 3:
            while y < N:
                if graph[x][y] == 'S':
                    return False
                elif graph[x][y] == 'O':
                    return True
                y += 1
        x, y = xx, yy
    return True

for i in list(combinations(x, 3)):
    sw = 0
    for x, y in i:
        graph[x][y] = 'O'

    for x, y in t:
        if watch(x, y):
            sw += 1

    if sw == len(t):
        break

    for x, y in i:
        graph[x][y] = 'X'

if sw == len(t):
    print("YES")
else:
    print("NO")