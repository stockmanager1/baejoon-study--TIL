m,n = input().split()
m= int(m)
n = int(n)

list_A = set(list(map(int,input().split())))
list_B = set(list(map(int,input().split())))

A =list_A.difference(list_B)
B =list_B.difference(list_A)
print(len(A)+len(B))