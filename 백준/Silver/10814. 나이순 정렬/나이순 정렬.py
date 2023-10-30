n = int(input())

people = []

for i in range(n):
  a,m = input().split()
  a = int(a)
  people.append([a,m])

people.sort(key=lambda x: (x[0]))

for i in people:
  print(*i)