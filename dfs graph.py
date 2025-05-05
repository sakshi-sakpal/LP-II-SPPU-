# Depth First Search in an Undirected Graph

# Create the graph using a dictionary (adjacency list)
graph = {
    'A': ['B', 'C'],
    'B': ['A', 'D', 'E'],
    'C': ['A', 'F'],
    'D': ['B'],
    'E': ['B', 'F'],
    'F': ['C', 'E']
}

# DFS function using recursion
def dfs(graph, start, visited=None):
    if visited is None:
        visited = set()
    
    print(start, end=' ')  # Process the node
    visited.add(start)
    
    for neighbor in graph[start]:
        if neighbor not in visited:
            dfs(graph, neighbor, visited)

# Run DFS
print("DFS Traversal starting from vertex A:")
dfs(graph, 'A')
