n = int(input())
cnt = 0
set_A = set()


for i in range(n):
  words = input()
  if words == 'ENTER':
      cnt = len(set_A) + cnt
      set_A = set()
  else:
    set_A.add(words)
print(len(set_A) + cnt)