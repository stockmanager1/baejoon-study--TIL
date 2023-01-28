m,n = input().split()
m = int(m)
n = int(n)

list_dict = {}
find_list =[]
i = 0
key_list=[]
value_list = []
while True:
  if i == (m+n):
    break
  else:
    if i < m:
      k = input().split(' ')
      key_list.append(k[0])
      value_list.append(k[1])
      i = i + 1
    elif m <= i < m+n:
      find_list.append(input())
      i = i + 1

list_dict = { name:value for name, value in zip(key_list, value_list) }

for i in range(n):
  print(list_dict[find_list[i]])