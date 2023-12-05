def DFSR(adj,s,visited):
    visited[s]=True
    print(s,end=' ')
    for u in adj[s]:
        if visited[s]==False:
            DFSR(adj,s,visited)
def DFS(adj):
    visited=[False]*len(adj)
    for u in range(len(adj)):
        if visited[u]==False:
            DFSR(adj,u,visited)
adj = [[1, 2], [0, 2], [0, 1], [4], [3]]
DFS(adj)    