from sys import stdin

a,b,c,d,e,f = map(int, stdin.readline().strip().split())


print((c*e-b*f)//(a*e-b*d), (a*f-d*c)//(a*e-b*d))