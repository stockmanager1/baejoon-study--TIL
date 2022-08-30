n = int(input())
LIST=[]
for i in range(n):
  LIST.append(input().split())

LIST.sort(key = lambda x:int(x[0]))
for i in LIST:
  print(*i)