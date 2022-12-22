n = int(input())
k = n
i = 1
while True:
  k= str(k)
  k_list = list(k)
  k_list = list(map(int,k_list))
  k_sum = sum(k_list)
  k_sum = str(k_sum)
  k_sum = list(k_sum)
  value = str(k_list[-1]) + k_sum[-1]
  value = int(value)
  k = value
  if n == value:
    print(i)
    break
  else:
    i = i + 1