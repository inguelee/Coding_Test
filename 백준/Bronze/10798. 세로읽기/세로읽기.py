from sys import stdin

s = [[''] * 15 for _ in range(5)]
for i in range(5):
    ip = tuple(stdin.readline().strip())
    for j in range(len(ip)):
        s[i][j] = ip[j]

for i in range(15):
    for j in range(5):
        print(s[j][i], end='')