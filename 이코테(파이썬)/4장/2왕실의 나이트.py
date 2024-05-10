s = input()

s0 = ord(s[0]) - ord('a') + 1
s1 = int(s[1])
data = [(1, 2), (1, -2), (-1, 2), (-1, -2), (2, 1), (2, -1), (-2, 1), (-2, -1)]
result = 0

for i in data:
    x = s0 + i[0]
    y = s1 + i[1]
    if 0 < x < 9 and 0 < y < 9:
        result += 1

print(result)