n = int(input())
m = int(input())
k = []
for q in range(n,m+1):
  k.append(q)
A = []
for i in k:
  if i == 2:
    A.append(i)
  for j in range(2,i):
    if i % j == 0:
      break
    if j == i-1 and (i-1) % j == 0:
        A.append(i)
if len(A) >= 1:
  print(sum(A))
  print(min(A))
else:
  print(-1)