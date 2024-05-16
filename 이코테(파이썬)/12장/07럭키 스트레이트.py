N = input()
a = sum(map(int, N[:len(N)//2]))
b = sum(map(int, N[len(N)//2:]))

if a == b:
    print("LUCKY")
else:
    print("READY")