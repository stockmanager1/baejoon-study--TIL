n = input()

list_A = list(n)

list_B = []

for i in range(len(n)):
  k = ''.join(list_A[i:])
  list_B.append(k)
    
list_B = sorted(list_B)

for i in list_B:
  print(i)