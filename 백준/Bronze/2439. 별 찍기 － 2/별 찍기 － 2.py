n = input()
n = int(n)
A = []
for i in range(0,n):
  A.append(' ')
i = 1

while i <= len(A):
  A[len(A)-i] = '*'
  i = i + 1
  B = ''.join(A)
  print(B)