from sys import stdin

array = []
for _ in range(int(stdin.readline())):
    array.append(int(stdin.readline()))

c = 0
m = 0

while array:
    mm = array.pop()
    if m < mm:
        m = mm
        c += 1
        
print(c)