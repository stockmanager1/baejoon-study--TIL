import sys

n,m =  map(int,sys.stdin.readline().split())


nums  = list(map(int,sys.stdin.readline().split()))

pre = [0]
mysum = 0

for i in range(n):
  mysum += nums[i]
  pre.append(mysum)
    
    
for i in range(m):
  a, b =  map(int,sys.stdin.readline().split())
  print(pre[b] - pre[a-1])