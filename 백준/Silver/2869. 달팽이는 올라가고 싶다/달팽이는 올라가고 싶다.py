import math
A,B,C = input().split()
A = int(A)
B = int(B)
C = int(C)

all_length = C - A
go_length = A - B
if A == C:
  print(1)
else:
  print(int(math.ceil(all_length / go_length)) + 1)