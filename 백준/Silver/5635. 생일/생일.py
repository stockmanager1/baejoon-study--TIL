n = int(input())

list_A = []

for i in range(n):
  list_A.append(input().split())

for i in range(n):
  list_A[i][1] = int(list_A[i][1])
  list_A[i][2] = int(list_A[i][2])
  list_A[i][3] = int(list_A[i][3])

list_A.sort(key=lambda x: (x[3],x[2],x[1]))

print(list_A[-1][0])
print(list_A[0][0])