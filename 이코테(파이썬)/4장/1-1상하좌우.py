N = int(input())
A = input().split()

dx = [0, 1, 0,-1]
dy = [1, 0,-1, 0]
x, y = 1, 1
d = 0
#     R  D  L  U
#     0  1  2  3

for i in A:
    if i == 'R':
        d = 0
    elif i == 'D':
        d = 1
    elif i == 'L':
        d = 2
    elif i == 'U':
        d = 3
    
    nx = x + dx[d]
    ny = y + dy[d]

    if 0 < nx <= N and 0 < ny <= N:
        x, y = nx, ny

print(x, y)