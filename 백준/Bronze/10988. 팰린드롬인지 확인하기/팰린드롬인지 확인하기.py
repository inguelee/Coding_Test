from sys import stdin

s = stdin.readline().strip()
sw = 1

for i in range((len(s) // 2) + 1):
    if s[i] != s[len(s)-i-1]:
        sw = 0
        break

print(sw)