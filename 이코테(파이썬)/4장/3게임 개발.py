N, M = map(int, input().split())
A, B, direction = map(int, input().split())
data = list()
for _ in range(N):
    data.append(list(map(int, input().split())))

result = 1
data[A][B] = 2
dx = [-1,0, 1, 0]
dy = [0, 1, 0,-1]
c = 0

def turn_left():
    global direction
    direction -= 1
    if direction == -1:
        direction = 3

while True:
    turn_left()
    nx = A + dx[direction]
    ny = B + dy[direction]
    c += 1
    if data[nx][ny] == 0:
        A, B = nx, ny
        data[nx][ny] = 2
        result += 1
        c = 0
    
    if c == 4:
        nx = A - dx[direction]
        ny = B - dy[direction]
        A, B = nx, ny
        c = 0
        if data[nx][ny] == 1:
            break

print(result)