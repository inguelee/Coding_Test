data = []
for i in range(int(input())):
    a = int(input())
    if a:
        data.append(a)
    else:
        data.pop()
        
print(sum(data))