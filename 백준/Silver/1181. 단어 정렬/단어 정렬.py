n = int(input())
old_list = []
for i in range(n):
  old_list.append(input())

old_list = set(old_list)

final_dict = {}
for i in old_list:
  K = list(i)
  final_dict[i] = len(K)



sorted_dict = sorted(final_dict.items(), key = lambda x : (x[1],x[0]))



for j in sorted_dict:
  print(j[0])