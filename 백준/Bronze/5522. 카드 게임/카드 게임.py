list_A = []
try:
  while True:
    list_A.append(int(input()))
except:
  pass

print(sum(list_A))