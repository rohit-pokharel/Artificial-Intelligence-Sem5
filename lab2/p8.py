import random

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

def misplaced_tiles(state):
    """Count misplaced tiles compared to the goal state."""
    count = 0
    for r in range(3):
        for c in range(3):
            if state[r][c] != goal_state[r][c] and state[r][c] != 0:
                count += 1
    return count

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

def steepest_ascent_hill_climbing(start_state, heuristic_fn):
    """Solve the 8-puzzle using Steepest Ascent Hill Climbing algorithm."""
    current_state = start_state
    current_heuristic = heuristic_fn(current_state)
    
    while True:
        neighbors = get_neighbors(current_state)
        best_neighbor = None
        best_heuristic = float('inf')
        
        # Evaluate all neighbors and choose the best one based on the heuristic
        for neighbor in neighbors:
            neighbor_heuristic = heuristic_fn(neighbor)
            if neighbor_heuristic < best_heuristic:
                best_neighbor = neighbor
                best_heuristic = neighbor_heuristic
        
        # If no better neighbor is found, return the current state
        if best_heuristic >= current_heuristic:
            return current_state
        
        # Otherwise, move to the best neighbor
        current_state = best_neighbor
        current_heuristic = best_heuristic

def print_state(state):
    """Print the state of the puzzle."""
    for row in state:
        print(row)
    print()

# Example usage:
start_state = ((1, 2, 3), (8, 0, 4), (7, 6, 5))  # Example starting state

# Apply the steepest ascent hill climbing with Manhattan distance heuristic
solution = steepest_ascent_hill_climbing(start_state, manhattan_distance)

print("Solution found:")
print_state(solution)
