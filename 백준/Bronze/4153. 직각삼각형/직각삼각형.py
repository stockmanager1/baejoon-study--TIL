while True:

  a,b,c = input().split()
  a = int(a)
  b = int(b)
  c = int(c)
  A = [a,b,c]

  if a==0 and  b==0 and c==0:
    break
  c = []
  max_A = max(A)
  A.remove(max_A)
  for i in A:
    c.append(i*i)
  if max_A * max_A == sum(c):
    print('right')
  else:
    print('wrong')