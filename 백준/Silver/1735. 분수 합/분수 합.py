from fractions import Fraction

m,n = input().split()
m = int(m)
n = int(n)

a,b = input().split()

a = int(a)
b = int(b)

k = Fraction(m, n)+Fraction(a, b)

분자 = k.numerator
분모 = k.denominator

print(분자, 분모)