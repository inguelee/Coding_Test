S = input()

result = int(S[0])

for i in S[1:]:
    if result < 2 or int(i) < 2:
        result += int(i)
    else:
        result *= int(i)

print(result)