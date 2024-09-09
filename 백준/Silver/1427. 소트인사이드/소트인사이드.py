from sys import stdin

n = list(stdin.readline().strip())
n.sort(reverse=True)
print(''.join(n))