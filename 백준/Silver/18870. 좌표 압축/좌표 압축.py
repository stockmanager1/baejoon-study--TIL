n = int(input())
좌표 = list(map(int,input().split()))

좌표1 = set(좌표)
좌표1 = list(좌표1)

좌표1.sort()

좌표순서 = []
for i in range(len(좌표1)):
  좌표순서.append(i)

key = []
value = []
for i,j in enumerate(좌표1,0):
  value.append(i)
  key.append(j)
diction = dict(zip(key,value))

result = []
for i in 좌표:
  result.append(diction.get(i))
print(*result)