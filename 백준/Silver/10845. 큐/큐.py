import sys
n= int(sys.stdin.readline())
stack = []

for i in range(n):
  a = sys.stdin.readline().split()
  if len(a) == 2:
    stack.append(a[1])
  else:
    if a[0] == 'pop':
      if len(stack) == 0:
        print(-1)
      else:
        print(stack[0])
        del stack[0]
    elif a[0] == 'size':
      print(len(stack))
    elif a[0] == 'empty':
      if len(stack) == 0:
        print(1)
      else:
        print(0)
    elif a[0] == 'front':
      if len(stack) == 0:
        print(-1)
      else:
        print(stack[0])
    elif a[0] == 'back':
      if len(stack) == 0:
        print(-1)
      else:
        print(stack[len(stack)-1])