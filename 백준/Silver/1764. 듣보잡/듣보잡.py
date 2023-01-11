from collections import Counter


m,n = input().split()
m = int(m)
n = int(n)

list_A = []

for i in range(m+n):
  list_A.append(input())

cnt = Counter(list_A)

list_B = []

for i in cnt.keys():
  if cnt[i] >= 2:
    list_B.append(i)
    
    
list_B = sorted(list_B)


print(len(list_B))
for i in list_B:
  print(i)