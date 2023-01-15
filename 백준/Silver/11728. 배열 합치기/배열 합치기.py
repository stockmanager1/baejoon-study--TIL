m,n = input().split()
m = int(m)
n = int(n)

list_A = input().split()
list_B = input().split()

list_A = list(map(int,list_A))
list_B = list(map(int,list_B))


list_C = []

for i in range(m):
  list_C.append(list_A[i])

for i in range(n):
  list_C.append(list_B[i])

list_C = sorted(list_C)
print(*list_C)
