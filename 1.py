graph={
    
}
visited=set()
def dfs(visited,graph,node):
    if node not in visited:
        print(node,end=' ')
        visited.add(node)
        for i in graph[node]:
            if i:
                dfs(visited,graph,i)
dfs(visited,graph,'1')