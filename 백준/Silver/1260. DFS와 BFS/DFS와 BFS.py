n,m,v = input().split()
n = int(n)
m = int(m)
v = int(v)

list_A = []
dfs_list = []
bfs_list = []

for i in range(n+1):
  list_A.append([])

for i in range(m):
  input_list = input().split()
  input_list = list(map(int,input_list))
  list_A[input_list[0]].append(input_list[1])
  list_A[input_list[1]].append(input_list[0])

for i in range(len(list_A)):
  list_A[i] = sorted(list_A[i])

visited = [False]*len(list_A)


def dfs(graph, v, visited):
    # 현재 노드를 방문 처리
    visited[v] = True
    dfs_list.append(v)
    # 현재 노드와 연결된 다른 노드를 재귀적으로 방문
    for i in graph[v]:
        if not visited[i]:
            dfs(graph, i, visited)

dfs(list_A,v,visited)

visited.clear()

visited = [False]*len(list_A)


from collections import deque


def bfs(graph,start,visited):
  queue = deque([start])
  visited[start] = True

  while queue:
    v = queue.popleft()
    bfs_list.append(v)
    for i in graph[v]:
      if not visited[i]:
        queue.append(i)
        visited[i] = True

        
bfs(list_A,v,visited)



print(*dfs_list)
print(*bfs_list)