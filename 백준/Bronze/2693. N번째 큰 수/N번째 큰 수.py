n = int(input())
list_A = []
for i in range(n):
  list_A = list(map(int,input().split()))
  list_A = sorted(list_A,reverse=True)
  print(list_A[2])
