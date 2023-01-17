import sys

n = int(sys.stdin.readline())

cnt = 1

list_A = []

for i in range(n):
  a = int(sys.stdin.readline())
  for i in range(a):
    k = map(int,sys.stdin.readline().split())
    k = list(map(int,k))
    list_A.append(k)
  list_A = sorted(list_A, key = lambda x : (x[0]))
  cnt = 1
  for i in range(len(list_A)):
    if i == 0:
      value = list_A[i][1]
    else:
      q = list_A[i][1]
      if q < value:
        value = q
        cnt = cnt + 1
      else:
        pass
  print(cnt)
  list_A.clear()
  cnt = 1
