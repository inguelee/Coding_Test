N = int(input())
a = list(map(int, input().split()))
M = int(input())
b = list(map(int, input().split()))

for i in b:
    if i in a:
        print('yes', end=' ')
    else:
        print('no', end=' ')
