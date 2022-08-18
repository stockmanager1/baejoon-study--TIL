n = int(input())
A = []
for i in range(0,n):
  a = input()
  A.append(a)
D = []
for i in A:
  B = i.split()
  B = list(map(int,B))
  print
  sum = 0
  i = 1
  while i <=B[0]:
    sum = sum + B[i]
    i = i + 1
  C = sum/B[0]
  for k in B[1:]:
    if C < k:
      D.append(k)
    else:
      pass
  print("%0.3f%%" %((len(D)/B[0])*100))
  D.clear()