visited_states = []

# Heuristic function to calculate the value of the current state based on the goal state
def calculate_heuristic(current_state, goal_state):
    goal_state_column = goal_state[3]  # The goal column we're trying to match
    heuristic_value = 0

    # Compare each element in the current state with the goal state
    for i in range(len(current_state)):
        column = current_state[i]
        if column:  # If the column is not empty
            for j in range(len(column)):
                # Add positive value for correct element positions, negative for incorrect ones
                if column[j] != goal_state_column[j]:
                    heuristic_value -= j
                else:
                    heuristic_value += j
    return heuristic_value

# Generate the next state based on the current state and the previous heuristic value
def generate_next_state(current_state, prev_heuristic, goal_state):
    global visited_states

    # Make a copy of the current state
    state_copy = [column[:] for column in current_state]

    for i in range(len(state_copy)):
        temp_state = [column[:] for column in state_copy]  # Copy each sublist
        if temp_state[i]:  # If the column has elements to pop
            moved_element = temp_state[i].pop()  # Pop the last element
            for j in range(len(temp_state)):
                next_state = [column[:] for column in temp_state]  # Copy state again

                if j != i:  # Don't add the element to the same column it came from
                    next_state[j].append(moved_element)

                    # Only consider new states that have not been visited
                    if next_state not in visited_states:
                        current_heuristic = calculate_heuristic(next_state, goal_state)
                        if current_heuristic > prev_heuristic:  # Ensure we make progress
                            visited_states.append(next_state)  # Mark the state as visited
                            return next_state

    return None  # Return None if no valid next state is found

# Main function to solve the puzzle starting from the initial state
def solve_puzzle(initial_state, goal_state):
    global visited_states

    if initial_state == goal_state:  # If the initial state is already the goal, return it
        print(goal_state)
        print("Solution found!")
        return

    current_state = [column[:] for column in initial_state]  # Copy initial state

    while True:
        visited_states.append([column[:] for column in current_state])  # Mark the state as visited

        print(current_state)
        prev_heuristic = calculate_heuristic(current_state, goal_state)

        next_state = generate_next_state(current_state, prev_heuristic, goal_state)

        if next_state is None:  # If no valid next state is found, we are stuck
            print("Final state reached: ", current_state)
            return

        current_state = [column[:] for column in next_state]  # Move to the next state

# Entry point to start the solver
def solver():
    global visited_states
    initial_state = [[], [], [], ['B', 'C', 'D', 'A']]  # Initial state
    goal_state = [[], [], [], ['A', 'B', 'C', 'D']]  # Goal state
    solve_puzzle(initial_state, goal_state)

solver()
