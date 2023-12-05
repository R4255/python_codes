def addedge(adj,u,l):
    adj[u].append(l)
    adj[l].append(u)
def printgraph(adj):
    for u,l in enumerate(adj):
        print(u,"->",l)
v=4#these are the total number of the vertices 
adj=[[]for i in range(v)]
addedge(adj,0,1)
addedge(adj,0,2)
addedge(adj,1,2)
addedge(adj,1,3)
printgraph(adj)


