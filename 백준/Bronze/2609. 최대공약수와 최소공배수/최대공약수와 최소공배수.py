a1,a2 = input().split()
a1 = int(a1)
a2 = int(a2)

a1_list = []
a2_list = []

for i in range(1,a1+1):
  if a1 % i == 0:
    a1_list.append(i)
  else:
    pass

for i in range(1,a2+1):
  if a2 % i == 0:
    a2_list.append(i)
  else:
    pass

max_value = []
set_a1_list = set(a1_list)
set_a2_list = set(a2_list)

max_list = (set_a1_list & set_a2_list)
max_list = list(max_list)

print(max(max_list))

i = 1
j = 1
min_a1_list = []
min_a2_list = []
while True:
  num_1 = i * a1
  min_a1_list.append(num_1)
  i = i + 1
  num_2 = j * a2
  min_a2_list.append(num_2)
  j = j + 1
  set_a11_list = set(min_a1_list)
  set_a22_list = set(min_a2_list)
  max_list1 = (set_a11_list & set_a22_list)
  max_list1 = list(max_list1)
  if len(max_list1) == 1:
    print(max(max_list1))
    break
