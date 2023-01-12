def arr(list,v):
  list[0] = 0
  list[1] = 1
  for i in range(2,v+1):
    k = list[i-2] + list[i-1]
    list.append(k)

  print(k)
    
v = int(input())

list = [0,1]

if v == 0:
  print(0)
elif v == 1:
  print(1)
elif v >= 2:
  arr(list,v)