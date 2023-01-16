num = input()
x = [int(a) for a in str(num)]
if 0 not in x:
  print(-1)
else:
  x.remove(0)
  x = sorted(x,reverse=True)
  x= list(map(str,x))
  list_str = ''.join(x)
  list_int = int(list_str)
  k = str(list_int)+'0'
  k = int(k)
  if k % 3==0:
    print(k)
  else:
    print(-1)