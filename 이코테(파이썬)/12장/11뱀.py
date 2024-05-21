N = int(input())
m = [[0] * (N + 1) for _ in range(N + 1)]
for _ in range(int(input())):
    a, b = map(int, input().split())
    m[a][b] = 2
data = []
for _ in range(int(input())):
    X, C = input().split()
    data.append((int(X), C))

x, y = 1, 1
m[x][y] = 1
snack = [(x, y)]
dx = (-1,0, 1, 0)
dy = (0, 1, 0,-1)
#     0, 1, 2, 3
#     북,동,남,서
direction = 1
t = 0
sw = True

def turn(c):
    global direction
    if c == 'D':
        direction = (direction + 1) % 4
    else:
        direction = (direction - 1) % 4

for i in data:
    while i[0] != t:
        nx = x + dx[direction]
        ny = y + dy[direction]
        if 1 <= nx <= N and 1 <= ny <= N and m[nx][ny] != 1:
            if m[nx][ny] == 0:
                x, y = nx, ny
                m[x][y] = 1
                snack.append((x, y))
                px, py = snack.pop(0)
                m[px][py] = 0
            elif m[nx][ny] == 2:
                x, y = nx, ny
                m[x][y] = 1
                snack.append((x, y))
            t += 1
        else:
            sw = False
            break
        
        if i[0] == t:
            turn(i[1])

while sw:
    nx = x + dx[direction]
    ny = y + dy[direction]
    if 1 <= nx <= N and 1 <= ny <= N and m[nx][ny] != 1:
        if m[nx][ny] == 0:
            x, y = nx, ny
            m[x][y] = 1
            snack.append((x, y))
            px, py = snack.pop(0)
            m[px][py] = 0
        elif m[nx][ny] == 2:
            x, y = nx, ny
            m[x][y] = 1
            snack.append((x, y))
        t += 1
    else:
        sw = False
        break

print(t + 1)