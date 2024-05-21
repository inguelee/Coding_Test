N = input()

cnt = 0
if len(N) == 1:
    N = '0' + N
d = N

while True:
    a = d[0]
    b = d[1]
    c = int(a) + int(b)
    d = b + str(c%10)
    cnt += 1
    if N == d:
        break

print(cnt)