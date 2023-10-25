n = int(input())

list_A = []

for i in range(n):
  num = int(input())
  list_A.append(num)

list_A.sort()

for i in list_A:
  print(i)