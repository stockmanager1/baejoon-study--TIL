A,B,C,D = input().split()

A = int(A)
D = int(D)
C = int(C)
B = int(B)


E = C - A
F = D - B

G = [A,B,E,F]

print(min(G))