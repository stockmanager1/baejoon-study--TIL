m = int(input())
n = int(input())

list_A = input().split()
list_A = list(map(int,list_A))
list_A = sorted(list_A)
list_A

front = 0
rear = 1
cnt = 0
target = n

while True:
  if front >=m:
    break
  if rear >= m:
    front = front + 1
    rear = front + 1
  else:
    value = list_A[rear] + list_A[front]
    if value < target:
      rear = rear + 1
    elif value > target:
      front = front + 1
      rear = front + 1
    elif value == target:
      rear = rear + 1
      cnt = cnt + 1
print(cnt)