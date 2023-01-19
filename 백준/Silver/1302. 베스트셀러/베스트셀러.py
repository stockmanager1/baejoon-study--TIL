from collections import Counter
n = int(input())
list_A = []
for i in range(n):
  list_A.append(input())

cnt = Counter(list_A)
max_key = max(cnt,key=cnt.get)
max_value = cnt[max_key]
list_B = []
for i,j in cnt.items():
  if j == max_value:
    list_B.append(i)
  else:
    pass

list_B = sorted(list_B)
print(list_B[0])