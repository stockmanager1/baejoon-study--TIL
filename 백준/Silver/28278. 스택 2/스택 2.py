stack =  []
import sys
input = sys.stdin.readline
stack =  []

n = int(input())
for i in range(n):
  order_num = input().split()
  if int(order_num[0]) == 1:
    stack.append(int(order_num[1]))
  elif int(order_num[0]) == 2:
    if len(stack) == 0:
      print(-1)
    else:
      print(stack.pop())
  elif int(order_num[0]) == 3:
    print(len(stack))
  elif int(order_num[0]) == 4:
    if len(stack) == 0:
      print(1)
    else:
      print(0)
  elif int(order_num[0]) == 5:
    if len(stack) == 0:
      print(-1)
    else:
      print(stack[-1])          