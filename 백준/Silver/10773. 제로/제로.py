n= int(input())

num_list = []
for i in range(n):
  k = int(input())
  if k == 0:
    del num_list[len(num_list)-1]
  else:
    num_list.append(k)
print(sum(num_list))  