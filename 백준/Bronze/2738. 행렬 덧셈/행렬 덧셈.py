from sys import stdin
A = []
B = []
N, M = map(int, stdin.readline().strip().split())
for _ in range(N):
    A.append(list(map(int, stdin.readline().strip().split())))
    
for _ in range(N):
    B.append(list(map(int, stdin.readline().strip().split())))
    
for i in range(N):
    for j in range(M):
        print(A[i][j] + B[i][j], end=' ')
    print()