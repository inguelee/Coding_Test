n = int(input())

data = (500, 100, 50, 10, 5, 1)
s = 1000 - n
result = 0

for i in data:
    result += s // i
    s %= i
    
print(result)