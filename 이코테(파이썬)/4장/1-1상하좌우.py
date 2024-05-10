N = int(input())
A = input().split()

dX = {'L':-1, 'R':1}
dY = {'U':-1, 'D':1}
X, Y = 1, 1

for i in A:
    if i in dX:
        X += dX[i]
    elif i in dY:
        Y += dY[i]

    if X > N or X < 1:
        X -= dX[i]
    elif Y > N or Y < 1:
        Y -= dY[i]

print(Y, X)