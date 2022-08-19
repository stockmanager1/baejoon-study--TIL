n = int(input())

def 한수(n):
  B = []

  if 100<= n <= 1000:
    for i in range(100,n+1):
      if 100<= i <= 1000:
        pass
      else:
        break
      A = list(str(i))
      A = list(map(int,A))
      if A[0] <= A[1] <= A[2] and A[2] - A[1] == A[1] - A[0]:
        B.append(i)
      elif  A[0] >= A[1] >= A[2] and A[0] - A[1] == A[1] - A[2]:
        B.append(i)
  if 1 <= n <= 99:
    return n
  elif 100<= n <= 1000:
    return len(B)+9+90

print(한수(n))