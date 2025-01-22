import heapq

# Goal state for 8 puzzle
goal_state = ((1, 2, 3), (8, 0, 4), (7, 6, 5))

# Directions for possible tile moves (up, down, left, right)
directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]

def manhattan_distance(state):
    """Calculate Manhattan Distance heuristic."""
    distance = 0
    for r in range(3):
        for c in range(3):
            value = state[r][c]
            if value != 0:
                target_r, target_c = divmod(value - 1, 3)
                distance += abs(r - target_r) + abs(c - target_c)
    return distance

def get_neighbors(state):
    """Generate valid neighbors by sliding tiles."""
    neighbors = []
    zero_r, zero_c = next((r, c) for r in range(3) for c in range(3) if state[r][c] == 0)
    
    for dr, dc in directions:
        new_r, new_c = zero_r + dr, zero_c + dc
        if 0 <= new_r < 3 and 0 <= new_c < 3:
            new_state = list(list(row) for row in state)  # Create a copy of the state
            # Swap the empty space (0) with the adjacent tile
            new_state[zero_r][zero_c], new_state[new_r][new_c] = new_state[new_r][new_c], new_state[zero_r][zero_c]
            neighbors.append(tuple(tuple(row) for row in new_state))
    
    return neighbors

def a_star(start_state):
    """Solve the 8-puzzle using A* algorithm."""
    # Priority queue to store states to explore
    open_list = []
    # Start with the initial state, cost (g), and heuristic (h)
    heapq.heappush(open_list, (0 + manhattan_distance(start_state), 0, start_state, None))
    
    # Dictionary to track visited states
    visited = {}
    
    # A* loop
    while open_list:
        _, cost, current_state, parent = heapq.heappop(open_list)
        
        # If the goal is reached, return the path
        if current_state == goal_state:
            path = []
            while parent:
                path.append(current_state)
                current_state = parent
            path.append(goal_state)
            return path[::-1]
        
        if current_state not in visited:
            visited[current_state] = True
            for neighbor in get_neighbors(current_state):
                if neighbor not in visited:
                    heapq.heappush(open_list, (cost + 1 + manhattan_distance(neighbor), cost + 1, neighbor, current_state))
    
    return None  # No solution found

def print_solution(solution):
    """Print the solution path."""
    for step in solution:
        for row in step:
            print(row)
        print()

# Example usage:
start_state = ((1, 2, 3), (8, 0, 4), (7, 6, 5))  # Example starting state
solution = a_star(start_state)

if solution:
    print("Solution found:")
    print_solution(solution)
else:
    print("No solution found.")
