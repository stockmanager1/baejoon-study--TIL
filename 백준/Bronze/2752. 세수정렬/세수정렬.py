m,n,k = input().split()
m = int(m)
n = int(n)
k = int(k)

list_A=[]
list_A.append(m)
list_A.append(n)
list_A.append(k)

list_A = sorted(list_A)
print(*list_A)