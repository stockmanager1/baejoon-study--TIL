n = int(input())
list_A = []
for i in range(1,n+1):
  list_A.append(i)

from itertools import permutations


for i in permutations(list_A): 
	print(*i)