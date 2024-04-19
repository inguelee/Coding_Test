N = int(input())
data = ()
array = []

for i in range(N):
    A, B = input().split()
    data = (A,int(B))
    array.append(data)

def sw(data):
    return data[1]

array.sort(key=sw)

for i in array:
    print(i[0], end=' ')