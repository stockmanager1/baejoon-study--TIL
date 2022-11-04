n = int(input())

num_list = []
first = 0
second = 1
num_list = [0,1]
for i in range(0,n+1):
  if len(num_list) > n :
    break
  else:
    k = num_list[len(num_list)-2] + num_list[len(num_list)-1]
    num_list.append(k)
  

if n == 0:
  print(0)
else:
  
 print(num_list[len(num_list)-1])