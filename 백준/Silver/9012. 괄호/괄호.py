A = int(input())

list_A = []
list_C = []
for i in range(A):
  n = input()
  n = list(n)

  for i in n:
    list_A.append(i)
    if len(list_A) >=2 and list_A[len(list_A)-2] == '(' and list_A[len(list_A)-1] == ')':
      list_A.remove(list_A[len(list_A)-2])
      list_A.remove(list_A[len(list_A)-1])
    else:
      pass
  if len(list_A) != 0:
    list_C.append('NO')
    list_A.clear()
  else:
    list_C.append('YES')
    list_A.clear()

for i in list_C:
  print(i)