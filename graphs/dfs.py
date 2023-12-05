def DFS(adj,s,visited):
    visited[s] = True
    print(s,end=' ')
    for element in adj[s]:
        if visited[element]==False:
            DFS(adj,element,visited)
def DFSg(adj,s):
    visited=[False]*len(adj)
    DFS(adj,s,visited)
def printgraph(adj):
    for u,l in enumerate(adj):
        print(u,'->',l)
adj=[[1,2],[0,3,4],[0,3],[1,2,4],[1,3]]
printgraph(adj)
DFSg(adj,0)