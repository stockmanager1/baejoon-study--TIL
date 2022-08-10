import sys
A = int(sys.stdin.readline())
B = []
for i in range(0,A):
  C = int(sys.stdin.readline())
  B.append(C)

B = sorted(B)

for i in B:
  print(i)