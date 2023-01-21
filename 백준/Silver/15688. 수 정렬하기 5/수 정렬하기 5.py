import sys
n= int(sys.stdin.readline())
list_A = []
for i in range(n):
  list_A.append(int(sys.stdin.readline()))


list_A = sorted(list_A)

for i in list_A:
  print(i)