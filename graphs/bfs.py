#main idea is to push a node first 
#mark it as visited and push its adjacency elements
#also we will maintain a visited queue 
from collections import deque
def addedge(adj,u,v):
    adj[u].append(v)
    adj[v].append(u)
def printgraph(adj):
    for u,v in adj:
        print(u,"->",v)
def BFS(source,adj):
    q=deque()
    q.append(source)
    visited=[False]*len(adj)
    visited[source]=True
    while q:
        s=q.popleft()
        print(s,end=" ")
        for element in adj[s]:
            if visited[element]==False:
                q.append(element)
                visited[element]=True
v=4
adj=[[1, 2], [0, 2, 3], [0, 1, 3, 4], [1, 2, 4], [2, 3]]
BFS(0,adj)

