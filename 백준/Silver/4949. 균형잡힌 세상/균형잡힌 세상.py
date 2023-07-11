while True:
  words = input()
  stack = []
  if words == '.':
    break
  else:
    for i in words:
      if i == '(' or i == '[':
        stack.append(i)
      elif i == ')':
        if len(stack) != 0 and stack[-1] == '(':
          stack.pop()
        else:
          stack.append(i)
      elif i == ']':
        if len(stack) != 0 and stack[-1] == '[':
          stack.pop()
        else:
          stack.append(i)
  if len(stack) == 0:
    print('yes')
  else:
    print('no')
