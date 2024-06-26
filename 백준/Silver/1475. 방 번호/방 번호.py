from sys import stdin

N = list(map(int, stdin.readline().strip()))
result = 1
check = [0 for _ in range(10)]

for i in N:
    check[i] += 1

if check.index(max(check)) == 6 or check.index(max(check)) == 9:
    b = max(check[6], check[9])
    c = min(check[6], check[9])
    while abs(b-c) > 1:
        b -= 1
        c += 1  
    check[6] = b
    check[9] = c

print(max(check))