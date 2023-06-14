n = int(input())
dict = {}
for i in range(n):
  words = input()
  if words in dict:
    dict[words].append('참여')
  else:
    dict[words] = ['참여']


for i in range(n-1):
  del_words = input()
  dict[del_words].remove('참여')
  if len(dict[del_words]) == 0:
    del dict[del_words]
print(list(dict.keys())[0])