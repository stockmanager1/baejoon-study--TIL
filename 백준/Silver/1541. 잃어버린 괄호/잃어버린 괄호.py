n = input().split('-')

list_A = []

for i in n:
  k = i.split('+')
  if len(k) == 1:
    k = int(k[0])
    list_A.append(k)
  else:
    k = list(map(int,k))
    k = sum(k)
    list_A.append(k)
cnt = list_A[0]
for i in range(1,len(list_A)):
  cnt = cnt- list_A[i]
print(cnt)