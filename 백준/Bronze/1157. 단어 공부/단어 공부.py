n = input()
a = n.upper()
a = list(a)
k = []
for i in a:
  if i not in k:
    k.append(i)
b = 0
c =[]
while b < len(k):
  c.append(a.count(k[b]))
  b = b + 1


if c.count(max(c)) >= 2:
  print("?")
else: print(k[c.index(max(c))])