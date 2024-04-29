S = input()

SS = ord(S[0]) - 96, int(S[1])
result = 0
data = [(2, 1), (2, -1), (-2,1), (-2,-1), (1,2),(1,-2), (-1,2), (-1,-2)]

for i in data:    
    a = SS[0] + i[0]
    b = SS[1] + i[1]
    if 0 < a < 9 and 0 < b < 9:
        result += 1
print(result)