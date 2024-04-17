N = int(input())
A = input().split()
d = {'L':-1, 'R':1, 'U':-1, 'D':1}
X, Y = 1, 1
for i in A:
    if i == 'L' or i == 'R':
        Y += d[i]
    else:
        X += d[i]

    if X > N or X < 1:
        X -= d[i]
    elif Y > N or Y < 1:
        Y -= d[i]

print(X, Y)
