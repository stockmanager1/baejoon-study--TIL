import sys
sys.setrecursionlimit(10**6)  

def dfs(node, parent, graph, parents):
    parents[node] = parent  
    for child in graph[node]:
        if parents[child] == 0:  
            dfs(child, node, graph, parents)


n = int(input())
graph = [[] for _ in range(n+1)]  
parents = [0] * (n+1)  

for _ in range(n-1):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)


dfs(1, 0, graph, parents)  


for i in range(2, n+1):
    print(parents[i])
