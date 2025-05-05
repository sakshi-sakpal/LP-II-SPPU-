def find(parent, node):
    if parent[node] != node:
        parent[node] = find(parent, parent[node])
    return parent[node]

def union(parent, rank, u, v):
    root_u = find(parent, u)
    root_v = find(parent, v)
    if root_u != root_v:
        if rank[root_u] < rank[root_v]:
            parent[root_u] = root_v
        elif rank[root_u] > rank[root_v]:
            parent[root_v] = root_u
        else:
            parent[root_v] = root_u
            rank[root_u] += 1

def kruskal(nodes, edges):
    edges.sort(key=lambda x: x[2])
    parent = {node: node for node in nodes}
    rank = {node: 0 for node in nodes}
    mst_cost = 0

    for u, v, weight in edges:
        if find(parent, u) != find(parent, v):
            union(parent, rank, u, v)
            mst_cost += weight
    return mst_cost

nodes = ['A', 'B', 'C', 'D']
edges = [('A', 'B', 1), ('A', 'C', 3), ('B', 'C', 1), ('B', 'D', 6), ('C', 'D', 2)]
print("Kruskal's MST Cost:", kruskal(nodes, edges))
