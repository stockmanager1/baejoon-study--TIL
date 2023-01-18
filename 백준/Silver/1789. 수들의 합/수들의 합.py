n = int(input())

i = 1

k = 0

while True:
  if k > n:
    print(i-2)
    break
  else:
    k = k + i
    i = i + 1