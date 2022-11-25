n = int(input())

i = 0
final = []


while True:
  if n < i * 5:
    break
  rest_value = n - 5*i
  if rest_value % 3 != 0:
    pass
  else:
    value = rest_value // 3
    final.append(i + value)
  i = i + 1
if len(final) == 0:
  print(-1)
else:
  print(min(final))