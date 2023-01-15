m,n = input().split()

m = int(m)
n = int(n)

list_A = input().split()

list_A = list(map(int,list_A))

list_A = sorted(list_A)

print(list_A[n-1])