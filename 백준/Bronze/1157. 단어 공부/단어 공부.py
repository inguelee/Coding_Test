from collections import Counter

s = input().upper()
if len(Counter(s).most_common()) == 1:
    print(Counter(s).most_common()[0][0])
elif Counter(s).most_common()[0][1] == Counter(s).most_common()[1][1]:
    print('?')
else:
    print(Counter(s).most_common()[0][0])