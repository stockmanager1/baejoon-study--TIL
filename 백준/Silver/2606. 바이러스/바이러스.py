m = int(input())
n = int(input())
graph = [[]]

for i in range(m):
  graph.append([])

for i in range(n):
  num = list(map(int,input().split()))
  graph[num[0]].append(num[1])
  graph[num[1]].append(num[0])

visited = [False] * (m+1)

dfs_list = []
def dfs(graph,v,visited):
  visited[v] = True
  dfs_list.append(v)
  for i in graph[v]:
    if not visited[i]:
      dfs(graph,i,visited)
    
dfs(graph,1,visited)

cnt = 0
for i in range(len(visited)):
  if visited[i] == True:
    cnt = cnt + 1
print(cnt-1)



