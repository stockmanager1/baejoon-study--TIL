n, k = input().split()
n = int(n)
k = int(k)

coin_list = []

for i in range(n):
  coin_list.append(input())
  
coin_list = list(map(int,coin_list))

coin_list_new = sorted(coin_list, reverse = True)

count=[]
for i in coin_list_new:
  if k < i:
    pass
  elif k >= i:
    count.append(k // i)
    k = k % i
print(sum(count))