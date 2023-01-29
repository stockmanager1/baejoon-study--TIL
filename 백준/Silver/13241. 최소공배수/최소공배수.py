import math
m,n = input().split()
m = int(m)
n = int(n)

def lcm(a,b):
  return (a * b) // math.gcd(a,b)

print(lcm(m,n))