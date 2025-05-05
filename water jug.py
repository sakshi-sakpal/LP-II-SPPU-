from collections import deque

def is_goal(state):
    return state[0] == 2 or state[1] == 2  # goal: get 2 liters in any jug

def get_next_states(current):
    a, b = current
    max_a, max_b = 4, 3
    next_states = []

    # Fill A or B
    next_states.append((max_a, b))
    next_states.append((a, max_b))

    # Empty A or B
    next_states.append((0, b))
    next_states.append((a, 0))

    # Pour A -> B
    pour = min(a, max_b - b)
    next_states.append((a - pour, b + pour))

    # Pour B -> A
    pour = min(b, max_a - a)
    next_states.append((a + pour, b - pour))

    return next_states

def water_jug_bfs():
    start = (0, 0)
    visited = set()
    queue = deque()
    queue.append((start, [start]))  # (state, path)

    while queue:
        state, path = queue.popleft()
        if state in visited:
            continue

        visited.add(state)

        if is_goal(state):
            return path  # solution found

        for next_state in get_next_states(state):
            if next_state not in visited:
                queue.append((next_state, path + [next_state]))

    return None  # no solution

# Run it
solution = water_jug_bfs()
if solution:
    print("Solution found:")
    for step in solution:
        print(f"Jug A: {step[0]}L, Jug B: {step[1]}L")
else:
    print("No solution.")
