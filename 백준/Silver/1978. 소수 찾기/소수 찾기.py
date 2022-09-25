n = int(input())
k = list(map(int,input().split()))


A = []
for i in k:
  if i == 2:
    A.append(i)
  for j in range(2,i):
    if i % j == 0:
      break
    if j == i-1 and (i-1) % j == 0:
        A.append(i)
    
print(len(A))