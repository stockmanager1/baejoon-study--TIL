import sys
n = int(sys.stdin.readline())
list_A = []
for i in range(1,n+1):
  list_A.append(int(sys.stdin.readline()))

list_A = sorted(list_A, reverse=True)
for i in list_A:
  print(i)