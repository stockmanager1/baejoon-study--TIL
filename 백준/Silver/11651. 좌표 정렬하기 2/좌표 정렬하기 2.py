n = int(input())
B = []
for i in range(0,n):
  A = list(map(int,input().split()))
  
  B.append(A)

C = sorted(B, key = lambda x: (x[1], x[0]))
for i in C:
  print(*i)