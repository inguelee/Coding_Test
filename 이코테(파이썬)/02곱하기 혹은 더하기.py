S = input()

result = 0
for i in S:
    if int(i) < 2 or result < 2:
        result += int(i)
    else:
        result *= int(i)

print(result)