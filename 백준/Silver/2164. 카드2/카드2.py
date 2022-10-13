n = int(input())

first_list = []

for i in range(1,n+1):
  first_list.append(i)
  
  
import collections
  
dequeue_first_list = collections.deque(first_list)


for i in first_list:
  if len(dequeue_first_list) == 1:
    break
  else:
    dequeue_first_list.remove(dequeue_first_list[0])
    dequeue_first_list.append(dequeue_first_list[0])
    dequeue_first_list.remove(dequeue_first_list[0])
    if len(dequeue_first_list) == 1:
        break
    
print(dequeue_first_list[0])