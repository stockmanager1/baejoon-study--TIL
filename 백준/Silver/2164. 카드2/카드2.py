n = int(input())
from collections import deque

card=deque([ ])

for i in range(1,n+1):
  card.append(i)
cnt = 1

while True:
  if len(card) == 1:
    print(card[0])
    break
  else:
    if cnt %2 == 0:
      num = card[0]
      card.popleft()
      card.append(num)
      cnt = cnt + 1
    else:
      card.popleft()
      cnt = cnt + 1