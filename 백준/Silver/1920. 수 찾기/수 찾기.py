A = int(input())
B = list(map(int,input().split()))
C = int(input())
D = list(map(int,input().split()))

B.sort()

def 이분탐색(array,target,start,end):
  while start <= end:
    mid = (start + end) // 2
    if array[mid] == target:
      return 1
    elif array[mid] > target:
      end = mid -1
    else:
      start = mid + 1
  return 0

for i in range(0,C):
  print(이분탐색(B,D[i],0,A-1))
