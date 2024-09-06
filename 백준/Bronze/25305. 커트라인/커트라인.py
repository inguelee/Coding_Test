from sys import stdin

N, k = map(int, stdin.readline().strip().split())
array = list(map(int, stdin.readline().strip().split()))

array.sort()
print(array[-k])