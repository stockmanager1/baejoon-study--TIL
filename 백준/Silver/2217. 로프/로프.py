n = int(input())
list_A=[]
for i in range(n):
  list_A.append(int(input()))

list_B = []

for i in range(n):
  if len(list_A) ==1:
    list_B.append(list_A[0])
    break
  else:
    list_A_min = min(list_A)
    list_B.append(len(list_A)*list_A_min)
    list_A.remove(list_A_min)

    
print(max(list_B))