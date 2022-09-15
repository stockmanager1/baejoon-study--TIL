A,B = input().split()
A = int(A)
B = int(B)

k=1
for i in range(1,A+1):
  k = k * i

j = 1
for i in range(1,B+1):
  j = j * i

z = 1
for i in range(1,(A-B)+1):
  z = z * i

print(int(k/(j*z)))