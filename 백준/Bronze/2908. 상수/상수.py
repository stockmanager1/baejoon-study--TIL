A, B = input().split()

A = list(A)
B = list(B)


A = list(reversed(A))
B = list(reversed(B))



A = ''.join(map(str,A))
B = ''.join(map(str,B))

A = int(A)
B = int(B)

if A > B:
  print(A)
else: 
  print(B)