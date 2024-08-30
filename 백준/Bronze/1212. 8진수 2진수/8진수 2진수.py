from sys import stdin

a = stdin.readline().strip()
b = '0o' + a

print(bin(int(b, 8))[2:])