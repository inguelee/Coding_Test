S = list(input())

result = int(S[0])

for i in S[1:]:
    if result < 1 or int(i) < 1:
        result += int(i)
    else:
        result *= int(i)

print(result)