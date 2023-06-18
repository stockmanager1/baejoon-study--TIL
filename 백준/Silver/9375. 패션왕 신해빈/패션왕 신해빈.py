n = int(input())

for i in range(n):
  cnt = 1
  set_clothes = {}
  t = int(input())
  for j in range(t):
    clothes = input().split()
    if clothes[1] not in set_clothes:
      set_clothes[clothes[1]] = []
      set_clothes[clothes[1]].append(clothes[0])
    else:
      set_clothes[clothes[1]].append(clothes[0])
  for k in set_clothes:
    cnt *= (len(set_clothes[k])+1)
  print(cnt-1)