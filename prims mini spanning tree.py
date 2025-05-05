import heapq

def prim(graph, start):
    visited = set()
    min_heap = [(0, start)]
    total_cost = 0

    while min_heap:
        cost, u = heapq.heappop(min_heap)
        if u in visited:
            continue
        visited.add(u)
        total_cost += cost
        for v, weight in graph[u]:
            if v not in visited:
                heapq.heappush(min_heap, (weight, v))
    return total_cost

graph = {
    'A': [('B', 1), ('C', 3)],
    'B': [('A', 1), ('C', 1), ('D', 6)],
    'C': [('A', 3), ('B', 1), ('D', 2)],
    'D': [('B', 6), ('C', 2)]
}
print("Prim's MST Cost:", prim(graph, 'A'))
