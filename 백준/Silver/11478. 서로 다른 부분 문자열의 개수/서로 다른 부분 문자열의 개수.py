n = input()

n = list(n)

num = len(n)

list_B =[]
i = 0
end = 1
start = 0

while True:
  if n[start:end] == n:
    filter = ''.join(filter)
    list_B.append(filter)
    break
  else:
    if end == len(n)+1:
      i =i + 1
      start = 0
      end  = i + 1
    else:
      filter = n[start:end]
      filter = ''.join(filter)
      start = start + 1
      end = end + 1
      list_B.append(filter)
list_B = list(set(list_B))
print(len(list_B)+1)