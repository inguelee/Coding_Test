N = int(input())
A = input().split()

X, Y = 1, 1
dataX = {'L':-1, 'R':1}
dataY = {'U':-1, 'D':1}

for i in A:
    if i in dataX:
        X += dataX[i]
    else:
        Y += dataY[i]
        
    if X > N or X < 1:
        X -= dataX[i]
    if Y > N or Y < 1:
        Y -= dataY[i]

print(Y, X)