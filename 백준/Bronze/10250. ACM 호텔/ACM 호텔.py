n = int(input())

for i in range(n):
  H,W,N = input().split()
  H = int(H)
  W = int(W)
  N = int(N)

  i = 1
  while True:
    if N - (H * i) <= 0:
      floor = i 
      break
    else:
      pass
    i += 1

  up_floor = N - H * (floor -1)

  if floor <= 9:
    up_floor = str(up_floor)
    floor = str(floor)
    print(up_floor + '0' + floor)
  else:
    up_floor = str(up_floor)
    floor = str(floor)
    print(up_floor + floor)