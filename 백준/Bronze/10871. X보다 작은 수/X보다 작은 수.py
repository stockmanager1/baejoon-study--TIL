count, factor = map(int, input().split(" "))
data = list(map(int, input().split(" ")))
k = []

for i in range(count):
    if factor > data[i]:
        k.append(data[i])
        
print(*k)