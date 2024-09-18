from sys import stdin

N, M = map(int, stdin.readline().strip().split())
a = []

for _ in range(N):
    array = list(stdin.readline().strip())
    array.reverse()
    a.append(array)
    
for i in range(N):
    b = ''.join(a[i])
    print(b)