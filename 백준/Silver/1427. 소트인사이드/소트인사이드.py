n = input()

n = list(n)

n = list(map(int,n))

n.sort(reverse=True)

n = list(map(str, n))

n = ''.join(n)
print(n)