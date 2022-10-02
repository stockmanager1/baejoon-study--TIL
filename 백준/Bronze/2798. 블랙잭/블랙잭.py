import random
import math
import itertools

A,B = input().split()
A = int(A)
B = int(B)
list_A = list(map(int,input().split()))

combine_list = []

k = itertools.combinations(list_A,3)
for i in k:
  a = list(i)
  b = sum(a)
  if b <= B:
    combine_list.append(b)
  else:
    pass

print(max(combine_list))