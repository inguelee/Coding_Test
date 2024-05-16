S = list(input())

S.sort()
n = 0

for i in range(len(S)):
    try:
        n += int(S[i])
    except:
        result = ''.join(S[i:]) + str(n)
        break

print(result)