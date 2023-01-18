m,n = input().split()
m = int(m)
n = int(n)

list_A = input().split()
list_A = list(map(int,list_A))

front = 0
rear = 0
target = n
cnt = 0

while (rear <= len(list_A)):
  if sum(list_A[front:rear]) < target:
    rear = rear + 1
  elif sum(list_A[front:rear]) > target:
    front = front + 1
  elif sum(list_A[front:rear]) == target:
    cnt = cnt + 1
    rear = rear + 1
    
print(cnt)
