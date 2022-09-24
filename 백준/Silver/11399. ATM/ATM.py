n = input()
n = int(n)
a = input().split()
a = list(map(int,a))
b = sorted(a)

c = []
d = []
for i in b:
  c.append(i)
  d.append(sum(c))
print(sum(d))