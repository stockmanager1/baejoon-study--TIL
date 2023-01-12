def pv(list,v):
  for i in range(2,v+1):
    k = list[i-2] + list[i-1]
    list.append(k)
  print(list[i])

v = int(input())
list = [0,1]

if v == 0:
  print(v)
elif v==1:
  print(v)
elif v>=2:
  pv(list,v)