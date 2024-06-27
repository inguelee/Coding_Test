from sys import stdin

big = 0
array = []
for i in range(9):
    result = tuple(map(int, stdin.readline().strip().split()))
    b = max(result)
    big = max(big, b)
    array.append(result)

for i in range(9):
    try:
        a = array[i].index(big)
        break
    except:
        continue

print(big)
print(i+1, a+1)