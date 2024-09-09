from sys import stdin

s = list(stdin.readline().strip())
array = ['a','e','i','o','u']
result = 0

for i in s:
    if i in array:
        result += 1

print(result)