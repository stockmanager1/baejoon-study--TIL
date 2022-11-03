n = int(input())
list_A = list(map(int,input().split()))

list_B = list_A.copy()

list_C = []

if len(list_A) == 1:
  print(list_A[0] * list_A[0])
else:
  value = max(list_B) * min(list_B)
  for i in list_A:
    if value % i == 0:
      list_C.append(i)
    else:
      list_B.remove(max(list_B))
      list_B.remove(min(list_B))
      break
  if len(list_A) == len(list_B):
    print(value)
