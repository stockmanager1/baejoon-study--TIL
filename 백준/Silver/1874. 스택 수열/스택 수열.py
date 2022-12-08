import sys 

n = int(sys.stdin.readline())

list_B = []

for i in range(n):
  list_B.append(int(sys.stdin.readline()))

list_B_cp = list_B.copy()

list_C = []
list_A = []
for i in range(1,n+1):
  list_A.append(i)
  list_C.append('+')
  while True:
    if len(list_A) == 0:
      break
    if list_A[-1] == list_B_cp[0]:
      list_A.remove(list_A[-1])
      list_B_cp.remove(list_B_cp[0])
      list_C.append('-')
    else:
      break
if len(list_B_cp) != 0:
  print('NO')
else:
  for i in list_C:
    print(i)