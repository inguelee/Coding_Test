S = list(input())

ss = 0
S.sort()

for i in range(len(S)):
    try:
        ss += int(S[i])
    except:
        result = ''.join(S[i:]) + str(ss)
        break
print(result)
