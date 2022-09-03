A = []
while True:
  i = int(input())
  A.append(i)
  if len(A) == 9:
    break
  i = i + 1

import random
while True:
  random_list = random.sample(A,7)
  if sum(random_list) == 100:
    break
random_list.sort()
for i in random_list:
  print(i)
