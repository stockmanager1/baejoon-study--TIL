while True:
  A = input()
  A = list(A)
  list_C = []
  if len(A) == 1 and A[0] == '0':
    break
  else:
    list_A = A[0:len(A)]
    list_B = A[::-1]
    for i,j in zip(list_A,list_B):
      if i != j:
        print('no')
        break
      else:
        list_C.append(i)
      if len(list_C) == len(list_A):
        print('yes')
