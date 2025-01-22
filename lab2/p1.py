import random

def display_environment(environment):
    for row in environment:
        print(row)

def vacuum_reflex_agent(environment):
    # Agent starts at the top-left corner of the grid (0, 0)
    rows, cols = len(environment), len(environment[0])
    current_position = (0, 0)

    while True:
        row, col = current_position

        # Display the current environment
        print(f"Agent is at position ({row}, {col})")
        display_environment(environment)

        # Sense the current room's state
        if environment[row][col] == 1:
            print(f"Room ({row}, {col}) is dirty. Cleaning...")
            environment[row][col] = 0
        else:
            print(f"Room ({row}, {col}) is already clean.")

        # Determine the next position
        if col + 1 < cols:
            # Move right if possible
            current_position = (row, col + 1)
        elif row + 1 < rows:
            # Move down to the next row if possible
            current_position = (row + 1, 0)
        else:
            # Stop if the agent has covered all rooms
            print("All rooms are clean!")
            break

# Generate a 3x3 environment with random 0s (clean) and 1s (dirty)
environment = [[random.choice([0, 1]) for _ in range(3)] for _ in range(3)]

print("Initial Environment:")
display_environment(environment)

# Run the vacuum cleaner agent
vacuum_reflex_agent(environment)

print("Final Environment:")
display_environment(environment)

