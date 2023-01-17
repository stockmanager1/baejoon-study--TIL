n = int(input())
    
list_A = []

for i in range(n):
  k=input().split()
  k[1] = int(k[1])
  k[2] = int(k[2])
  k[3] = int(k[3])
  list_A.append(k)

list_A = sorted(list_A, key = lambda x : (-x[1],x[2],-x[3],x[0]))


for i in range(len(list_A)):
  print(list_A[i][0])