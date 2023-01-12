import sys

input = sys.stdin.readline
n = int(input())
list_A = input().split()
list_A = list(map(int,list_A))
    

m = int(input())
list_B = input().split()
list_B = list(map(int,list_B))
    
from collections import Counter

cnt = Counter(list_A)

for i in range(len(list_B)):
  if list_B[i] in cnt.keys():
    list_B[i] = cnt[list_B[i]]
  else:
    list_B[i] = 0
        
print(*list_B)
