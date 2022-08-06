n = int(input())
A = []
for i in range(0,n):
  a = int(input())
  A.append(a)
A = sorted(A)
for i in A:
  print(i)
  
  
  #여기서 만약 주어진 수가 2가지라면 a,b = map(int,input().split())을 사용해야 한다
