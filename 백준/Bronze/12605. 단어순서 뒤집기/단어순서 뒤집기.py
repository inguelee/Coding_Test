from sys import stdin

for i in range(int(stdin.readline())):
    a = list(stdin.readline().strip().split())
    a.reverse()
    print(f"Case #{i + 1}: {' '.join(a)}")