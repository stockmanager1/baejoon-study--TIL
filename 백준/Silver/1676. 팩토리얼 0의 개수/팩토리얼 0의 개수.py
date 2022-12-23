n = int(input())
if n == 0:
  print(0)
else:

  for i in range(1,n+1):
    if i == 1:
      mul = i
    else:
      mul = mul * i
    
  mul_str = str(mul)

  mul_list= list(mul_str)

  cnt = 0

  for i in range(len(mul_list)+1):
    if mul_list[-1-i] == '0':
      cnt = cnt + 1
    else:
      break

  print(cnt)