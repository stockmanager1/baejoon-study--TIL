import sys
n = int(sys.stdin.readline())
list_A = list(map(int,sys.stdin.readline().split()))

list_A = sorted(list_A)
target = int(sys.stdin.readline())
list_A

front = 0
rear = 1
cnt = 0

while True:
  if front > n-1:
    break
  else:
    if rear >= n:
      front = front + 1
      rear = front + 1
    else:
      value = list_A[front] + list_A[rear]
      if value < target:
        rear = rear + 1
      elif value > target:
        front = front + 1
        rear = front + 1
      elif value == target:
        cnt = cnt + 1
        front = front + 1
        rear = front + 1
    
print(cnt)