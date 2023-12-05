from collections import deque
def addedge(adj,u,v):
    adj[u].append(v)
    adj[v].append(u)
def printgraph(adj):
    for u,l in enumerate(adj):
        print(u,"->",l)
def BFS(adj,s,visited):
    q=deque()
    q.append(s)
    visited[s]=True
    while q:
        t=q.popleft()
        print(t,end=' ')
        for element in adj[t]:
            if visited[element]==False:
                q.append(element)
                visited[element]=True
def BFSdis(adj):
    visited=[False]*len(adj)
    for u in range(len(adj)):
        if visited[u]==False:
            BFS(adj,u,visited)

v = 7

adj = [[1, 2], [0, 3], [0, 3], [1, 2], [5, 6], [4, 6], [4, 5]]

printgraph(adj)

print('\nBFS path')
BFSdis(adj)

