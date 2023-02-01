m,n = input().split()

m = int(m)
n = int(n)


S = []

for i in range(m):
  k = input().split()
  k = ''.join(k)
  S.append(k)


list_A =[]
for i in range(n):
  j = input().split()
  j = ''.join(j)
  list_A.append(j)

list_B =[]
for i in list_A:
  if i in S:
    list_B.append(i)
    
print(len(list_B))

