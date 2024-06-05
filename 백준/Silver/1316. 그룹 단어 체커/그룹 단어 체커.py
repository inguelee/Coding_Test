result = 0
def define(s):
    data = []
    if len(s) == 1:
        return True
    for i in range(len(s)-1):
        if s[i] != s[i + 1]:
            if s[i] in data or s[i + 1] in data:
                return False
            data.append(s[i]) 

    return True


for _ in range(int(input())):
    s = input()
    if define(s):
        result += 1

print(result)