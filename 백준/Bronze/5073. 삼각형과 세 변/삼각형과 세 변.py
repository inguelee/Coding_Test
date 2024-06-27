from sys import stdin
from collections import Counter

a, b, c = map(int, stdin.readline().strip().split())

while sum([a, b, c]):
    l = sorted([a, b, c], reverse=True)
    if l[0] >= l[1] + l[2]:
        print("Invalid")
    elif len(Counter([a, b, c])) == 1:
        print("Equilateral")
    elif len(Counter([a, b, c])) == 2:
        print("Isosceles")
    else:
        print("Scalene")

    a, b, c = map(int, stdin.readline().strip().split())