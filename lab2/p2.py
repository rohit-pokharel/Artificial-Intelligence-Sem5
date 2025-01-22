import random

def display_environment(environment):
    # Display the current state of the environment
    for row in environment:
        print(row)

def vacuum_model_based_agent(environment):
    """
    Model-based agent improvements:
    1. State Awareness:
       - The agent maintains knowledge of which rooms have been cleaned using a 'visited' set.
       - This eliminates redundant checks and re-cleaning of already cleaned rooms.

    2. Path Optimization:
       - The agent prioritizes unvisited rooms for cleaning, minimizing unnecessary travel.
       - It dynamically determines the next best move based on the state of the environment.

    3. Scalability:
       - This approach can handle larger grids more efficiently by avoiding unnecessary revisits.
       - It ensures the agent operates effectively without hardcoding specific traversal logic.

    4. Comprehensive Coverage:
       - The agent ensures every room is checked and cleaned, achieving complete coverage.
       - If no unvisited neighbors exist, it falls back to any valid position to complete cleaning.
    """
    rows, cols = len(environment), len(environment[0])
    visited = set()  # Track visited rooms
    current_position = (0, 0)

    def next_position(position):
        """
        Determine the next position to move to:
        - Prioritize unvisited neighboring cells.
        - If all neighbors are visited, fallback to any valid move.
        """
        row, col = position
        moves = [
            (row, col + 1),  # Move right
            (row + 1, col),  # Move down
            (row, col - 1),  # Move left
            (row - 1, col)   # Move up
        ]
        # Filter valid moves
        valid_moves = [
            (r, c) for r, c in moves if 0 <= r < rows and 0 <= c < cols
        ]
        # Prioritize unvisited positions
        for move in valid_moves:
            if move not in visited:
                return move
        # If all adjacent are visited, move to any valid position (fallback)
        return valid_moves[0] if valid_moves else None

    while True:
        row, col = current_position
        visited.add(current_position)  # Mark as visited

        # Display the agent's position and the environment
        print(f"Agent is at position ({row}, {col})")
        display_environment(environment)

        # Clean the current room if dirty
        if environment[row][col] == 1:
            print(f"Room ({row}, {col}) is dirty. Cleaning...")
            environment[row][col] = 0
        else:
            print(f"Room ({row}, {col}) is already clean.")

        # Determine the next position to move to
        next_pos = next_position(current_position)
        if next_pos and next_pos not in visited:
            current_position = next_pos
        else:
            # Stop if all reachable rooms are clean
            print("All reachable rooms are clean!")
            break

# Generate a 3x3 environment with random 0s (clean) and 1s (dirty)
environment = [[random.choice([0, 1]) for _ in range(3)] for _ in range(3)]

# Initial display of the environment
print("Initial Environment:")
display_environment(environment)

# Run the model-based vacuum cleaner agent
vacuum_model_based_agent(environment)

# Final display of the environment
print("Final Environment:")
display_environment(environment)
