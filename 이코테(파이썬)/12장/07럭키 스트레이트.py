N = input()

if len(N) % 2:
    print("READY")
else:
    a = N[:len(N)//2]
    b = N[len(N)//2:]

    a = list(map(int, a))
    b = list(map(int, b))

    if sum(a) == sum(b):
        print("LUCKY")
    else:
        print("READY")