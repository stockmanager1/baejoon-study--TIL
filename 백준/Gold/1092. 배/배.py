import sys
m = int(sys.stdin.readline())

list_A = list(map(int,sys.stdin.readline().split()))

n = int(sys.stdin.readline())
list_B = list(map(int,sys.stdin.readline().split()))
list_A = sorted(list_A,reverse=True)
list_B = sorted(list_B,reverse=True)
i = 0
cnt = 0
j= 0
while True:
  if list_A[0] < list_B[0]:
    print(-1)
    break
  if i == m:
    cnt = cnt + 1
    i = 0
    j = 0
  elif j == len(list_B):
    i = 0
    j = 0
    cnt= cnt + 1
  else:
    if list_A[i] >= list_B[j]:
      list_B.remove(list_B[j])
      if len(list_B) == 0:
        cnt = cnt + 1
        print(cnt)
        break
      else:
        i = i +1
    elif list_A[i] < list_B[j]:
      j = j + 1
      pass