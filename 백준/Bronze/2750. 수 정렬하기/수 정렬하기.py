n = int(input())
A = []
for i in range(0,n):
  a = int(input())
  A.append(a)
A = sorted(A)
for i in A:
  print(i)