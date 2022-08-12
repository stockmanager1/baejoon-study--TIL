n = input()
n = list(n)

k = []
for i in n:
  if i not in k:
    k.append(i)

    
i = 0

A = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']

while i <= len(A):
  if A[i] in n:
    A[i] = n.index(A[i])
  else:
    A[i] = -1
  i = i + 1
  if i == len(A):
    break
print(*A)