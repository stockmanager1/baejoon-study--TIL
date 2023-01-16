n = int(input())
list_A = input().split()
list_B = input().split()

list_A = list(map(int,list_A))
list_B = list(map(int,list_B))


list_A = sorted(list_A)
list_B = sorted(list_B, reverse=True)

k = []
for i,j in zip(list_A,list_B):
  k.append(i*j)

print(sum(k))

