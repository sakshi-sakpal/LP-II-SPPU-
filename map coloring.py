def is_safe(graph, colors, v, c):
    # Check all adjacent vertices
    for i in range(len(graph)):
        if graph[v][i] == 1 and colors[i] == c:
            return False
    return True

# Function to solve the graph coloring problem using backtracking
def graph_coloring_util(graph, m, colors, v):
    # If all vertices are assigned a color then return True
    if v == len(graph):
        return True
    
    # Try different colors for vertex v
    for c in range(1, m + 1):
        if is_safe(graph, colors, v, c):
            colors[v] = c
            if graph_coloring_util(graph, m, colors, v + 1):
                return True
            colors[v] = 0  # Backtrack
    
    return False

# Main function to solve the graph coloring problem
def graph_coloring(graph, m):
    # List to store the color assignment for each vertex
    colors = [0] * len(graph)
    
    # Call the graph coloring utility to check if it's possible to color the graph
    if graph_coloring_util(graph, m, colors, 0):
        print("Solution exists: The coloring of the graph is:")
        for i in range(len(graph)):
            print(f"Vertex {i + 1}: Color {colors[i]}")
    else:
        print("Solution does not exist")

# Example usage

# Adjacency matrix representation of the graph
# 0 1 1 1
# 1 0 1 0
# 1 1 0 1
# 1 0 1 0

graph = [
    [0, 1, 1, 1],  # Vertex 1 connected to 2, 3, 4
    [1, 0, 1, 0],  # Vertex 2 connected to 1, 3
    [1, 1, 0, 1],  # Vertex 3 connected to 1, 2, 4
    [1, 0, 1, 0]   # Vertex 4 connected to 1, 3
]

# Maximum number of colors allowed
m = 3  # For example, 3 colors

# Solve the graph coloring problem
graph_coloring(graph, m)