

n = int(input())
B = []
for i in range(0,n):
  A = list(map(int,input().split()))
  
  B.append(A)
B.sort()
for i in B:
  print(*i)