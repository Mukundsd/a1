graph = {
'A' : ['B','C'],
'B' : ['D', 'E'],
'C' : ['F'],
'D' : [],
'E' : ['F'],
'F' : []
}
visited = set() # Set to keep track of visited nodes of graph.
def dfs(visited, graph, node): #function for dfs
    if node not in visited:
        print (node)
    visited.add(node)
    for neighbour in graph[node]:
        dfs(visited, graph, neighbour)
# Driver Code

print("Name:Mukund Dhumal")
print("Batch:B3")
print("RollNo:61")
print("Following is the Path using Depth-First Search")
dfs(visited, graph, 'A')